class Solution:
    def frequencySort(self, s: str) -> str:
        to_sort = {}
        for ch in s:
            to_sort[ch] = to_sort.get(ch, 0) + 1

        pairs = sorted(to_sort.items(), key=lambda p: p[1], reverse=True)

        result = ""
        for ch, count in pairs:
            result += ch * count

        return result
