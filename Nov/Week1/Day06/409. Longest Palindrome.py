class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
        total = 0
        has_odd = False
        for count in freq.values():
            total += count - (count % 2)
            if count % 2 == 1:
                has_odd = True
        if has_odd:
            total += 1
        return total
