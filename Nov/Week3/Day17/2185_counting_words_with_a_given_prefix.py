from typing import List

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        counts = {}
        for word in words:
            for k in range(1, len(word) + 1):
                prefix = word[:k]
                counts[prefix] = counts.get(prefix, 0) + 1

        result = []
        for word in words:
            total = 0
            for k in range(1, len(word) + 1):
                total += counts[word[:k]]
            result.append(total)
        return result
