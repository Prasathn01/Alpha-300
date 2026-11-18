class Solution:
    def reorganizeString(self, s: str) -> str:
        rep = {}
        for ch in s:
            rep[ch] = rep.get(ch, 0) + 1

        maxf = max(rep.values())
        n = len(s)
        if maxf > (n + 1) // 2:
            return ""

        most_freq = ""
        for ch in rep:
            if rep[ch] == maxf:
                most_freq = ch

        asc_lis = [most_freq] * maxf
        for ch in rep:
            if ch != most_freq:
                asc_lis += [ch] * rep[ch]

        result = [""] * n
        pos = 0
        for ch in asc_lis:
            result[pos] = ch
            pos += 2
            if pos >= n:
                pos = 1

        return "".join(result)
