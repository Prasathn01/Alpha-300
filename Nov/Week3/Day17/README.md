# Day 17 - Prefix Sum Problems

## Problems Solved

1. **[2559. Count Vowel Strings in Ranges](https://leetcode.com/problems/count-vowel-strings-in-ranges/)**
   - Count vowel strings (starting and ending with vowels) in given ranges
   - Brute Force: Recalculate sum for each query - O(n*m)
   - Optimized: Prefix sum array for O(1) lookups - O(n+m)

2. **[2062. Count Vowel Substrings of a String](https://leetcode.com/problems/count-vowel-substrings-of-a-string/)**
   - Count substrings containing all 5 vowels exactly once
   - Approach: Nested loop with set tracking and early break

3. **[2185. Counting Words With a Given Prefix](https://leetcode.com/problems/counting-words-with-a-given-prefix/)**
   - Count sum of occurrences of all prefixes for each word
   - Approach: Prefix counting with dictionary to track frequency
