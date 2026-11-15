class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for k in range(1, n//2 + 1):
            if n % k != 0:
                continue
            for i in range(k, n):
                if s[i] != s[i - k]:
                    break
            else:
                return True
        return False
