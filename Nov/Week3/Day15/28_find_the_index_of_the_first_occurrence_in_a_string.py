class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        hay = len(haystack)
        need = len(needle)

        if need == 0:
            return 0
        if need > hay:
            return -1
        for i in range(hay - need + 1):
            for j in range(need):
                if haystack[i + j] != needle[j]:
                    break
            else:
                return i
        return -1
