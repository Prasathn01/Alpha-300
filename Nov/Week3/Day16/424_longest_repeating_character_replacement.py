class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        left = 0
        best = 0
        top = 0
        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1

            if freq[s[right]] > top:
                top = freq[s[right]]

            while right - left + 1 - top > k:
                freq[s[left]] -= 1
                left += 1

            if right - left + 1 > best:
                best = right - left + 1
        return best
