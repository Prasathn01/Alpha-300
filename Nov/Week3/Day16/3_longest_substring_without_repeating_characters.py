class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        longest = 0
        sett = set()
        n = len(s)

        for right in range(n):
            while s[right] in sett:
                sett.remove(s[left])
                left += 1

            w = (right -left) + 1
            longest = max(longest, w)
            sett.add(s[right])

        return longest
