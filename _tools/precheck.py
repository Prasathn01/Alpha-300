"""precheck.py - run before every commit.

Usage (from anywhere inside the repo):
    python _tools/precheck.py Nov/Week1/Day05
    python _tools/precheck.py Assignments/Oct-Bank/Set01

Checks the given folder and exits with code 1 if anything is wrong.
It only READS files. It never edits your code or your READMEs.
"""
import ast, os, re, subprocess, sys

PLACEHOLDERS = ["write this yourself", "<title>", "<file name>", "<problem title>",
                "<date>", "<topic>", "(same three lines)"]
FORBIDDEN = [
    (r"^\s*(import|from)\s+(collections|heapq|bisect|itertools|functools)\b", "forbidden import"),
    (r"(?<![\w.])sorted\s*\(", "built-in sorted()"),
    (r"\.sort\s*\(", ".sort()"),
    (r"\[\s*::\s*-1\s*\]", "[::-1] reversal"),
    (r"(?<![\w.])reversed\s*\(", "reversed()"),
]
SECRETS = r"ghp_[A-Za-z0-9]{20,}|github_pat_|AKIA[0-9A-Z]{12,}|sk-ant-|BEGIN [A-Z ]*PRIVATE KEY"

errors, warnings = [], []

def git(*args, cwd=None):
    r = subprocess.run(["git", *args], capture_output=True, text=True, cwd=cwd)
    return r.returncode, r.stdout.strip()

def code_part(line):
    # crude: drop everything after a # that is not inside quotes
    out, q = "", None
    for ch in line:
        if q:
            out += ch
            if ch == q: q = None
        elif ch in "'\"":
            q = ch; out += ch
        elif ch == "#":
            break
        else:
            out += ch
    return out

def check_py(path, rel):
    text = open(path, encoding="utf-8", errors="replace").read()
    body = [l for l in text.splitlines() if l.strip() and not l.strip().startswith("#")]
    if not body:
        errors.append(f"{rel}: file has no code (empty or comments only)")
        return
    try:
        ast.parse(text)
    except SyntaxError as e:
        errors.append(f"{rel}: syntax error on line {e.lineno}: {e.msg}")
    for n, line in enumerate(text.splitlines(), 1):
        c = code_part(line)
        for pat, label in FORBIDDEN:
            if re.search(pat, c):
                errors.append(f"{rel}:{n}: {label} is not allowed by the course")
        if re.search(SECRETS, line):
            errors.append(f"{rel}:{n}: looks like a secret or token")

def check_readme(path, rel):
    text = open(path, encoding="utf-8", errors="replace").read()
    low = text.lower()
    for p in PLACEHOLDERS:
        if p in low:
            errors.append(f"{rel}: still contains template text '{p}'")
    for need in ("approach", "edge case"):
        if need not in low:
            errors.append(f"{rel}: missing the '{need}' section")
    if not re.search(r"time\b", low) or not re.search(r"space", low):
        errors.append(f"{rel}: missing time and/or space complexity")
    if re.search(r"(time|space)[^\n]*:\s*$", text, re.I | re.M):
        errors.append(f"{rel}: a Time/Space line is empty")

def main():
    if len(sys.argv) != 2:
        print(__doc__); sys.exit(2)
    code, top = git("rev-parse", "--show-toplevel")
    if code != 0:
        print("Not inside a git repository."); sys.exit(2)
    target = os.path.normpath(os.path.join(os.getcwd(), sys.argv[1]))
    if not os.path.isdir(target):
        print(f"Folder not found: {sys.argv[1]}"); sys.exit(2)

    is_set = "assignments" in target.lower().replace("\\", "/")
    py_files, problem_dirs = [], []
    for dp, dn, fn in os.walk(target):
        for f in fn:
            full = os.path.join(dp, f)
            rel = os.path.relpath(full, top)
            if f.lower().endswith(".py"):
                py_files.append((full, rel))
            elif f.lower() == "readme.md":
                pass
            elif not f.startswith("."):
                warnings.append(f"{rel}: not a .py file (rename it to end in .py if it is a solution)")

    if not py_files:
        errors.append("no .py solution files found in this folder")
    for full, rel in py_files:
        check_py(full, rel)

    if is_set:
        for entry in sorted(os.listdir(target)):
            d = os.path.join(target, entry)
            if os.path.isdir(d):
                r = os.path.join(d, "README.md")
                if os.path.exists(r):
                    check_readme(r, os.path.relpath(r, top))
                else:
                    errors.append(f"{os.path.relpath(d, top)}: README.md missing")
    else:
        r = os.path.join(target, "README.md")
        if os.path.exists(r):
            check_readme(r, os.path.relpath(r, top))
            heads = len(re.findall(r"^## ", open(r, encoding="utf-8", errors="replace").read(), re.M))
            if heads < len(py_files):
                errors.append(f"{os.path.relpath(r, top)}: {len(py_files)} solution file(s) but only {heads} problem section(s)")
        else:
            errors.append(f"{os.path.relpath(target, top)}: README.md missing (copy _templates/day-README.md)")

    # repo-level safety
    gi = os.path.join(top, ".gitignore")
    gi_text = open(gi, encoding="utf-8", errors="replace").read() if os.path.exists(gi) else ""
    for local in ("LLM_PUSH_GUIDE.md", "CLAUDE.md", "AGENTS.md"):
        _, tracked = git("ls-files", local, cwd=top)
        if tracked:
            errors.append(f"{local} is tracked by git. Run: git rm --cached {local}")
        elif os.path.exists(os.path.join(top, local)) and local not in gi_text:
            errors.append(f".gitignore does not list {local}")
    _, venv_tracked = git("ls-files", ".venv", cwd=top)
    if venv_tracked:
        errors.append(".venv is tracked by git. Run: git rm -r --cached .venv")
    if os.path.isdir(os.path.join(top, ".venv")) and ".venv" not in gi_text:
        errors.append(".gitignore does not list .venv/")
    _, name = git("config", "user.name", cwd=top)
    _, email = git("config", "user.email", cwd=top)
    if not name or not email:
        errors.append("git user.name / user.email not set (git config --global ...)")

    print(f"Folder : {os.path.relpath(target, top)}")
    print(f"Author : {name} <{email}>   (this is who GitHub will show for your commits)")
    print(f"Files  : {len(py_files)} .py file(s)")
    for w in warnings: print("WARN  ", w)
    for e in errors:   print("ERROR ", e)
    if errors:
        print(f"\nFAILED with {len(errors)} error(s). Fix them, then run this again before committing.")
        sys.exit(1)
    print("\nPASSED. Safe to: git add . ; git commit ; git push")

main()
