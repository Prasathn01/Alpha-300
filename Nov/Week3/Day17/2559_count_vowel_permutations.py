from typing import List

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:

        vowels = "aeiou"
        test_1 = []
        for word in words:
            if word[0] and word[-1] in vowels:
                test_1.append(1)
            else:
                test_1.append(0)
        final = []
        for query in queries:
            left_index = query[0]
            right_index = query[1]
            total = 0
            for i in range(left_index, right_index + 1):
                total += test_1[i]
            final.append(total)
        return final
