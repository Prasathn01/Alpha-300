from typing import List

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:

        vowels = "aeiou"
        test_1 = []
        for word in words:
            if word[0] in vowels and word[-1] in vowels:
                test_1.append(1)
            else:
                test_1.append(0)

        prefix = [0]
        for flag in test_1:
            prefix.append(prefix[-1] + flag)

        final = []
        for query in queries:
            left_index = query[0]
            right_index = query[1]
            final.append(prefix[right_index + 1] - prefix[left_index])

        return final
