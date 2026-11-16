from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        need = {}
        for c in p:
            need[c] = need.get(c, 0) + 1

        win = {}
        res = []
        k = len(p)

        for i in range(len(s)):
            win[s[i]] = win.get(s[i], 0) + 1
            if i >= k:
                win[s[i - k]] -= 1
                if win[s[i - k]] == 0:
                    del win[s[i - k]]
            if win == need:
                res.append(i - k + 1)

        return res
