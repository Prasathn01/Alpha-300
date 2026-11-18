class Solution:
    def customSortString(self, order: str, s: str) -> str:
        string_1 = ""
        for ch in order:
            if ch in s:
                string_1 += ch * s.count(ch)

        string_2 = ""
        for ch in s:
            if ch not in order:
                string_2 += ch

        return string_1 + string_2
