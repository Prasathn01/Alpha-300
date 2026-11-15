# Day 15 -

## Problems Solved
1. **28. Find the Index of the First Occurrence in a String**
2. **[Problem Number]. [Problem Title]**
3. **[Problem Number]. [Problem Title]**

---

## Problem 1: Find the Index of the First Occurrence in a String
**LeetCode:** [28. Find the Index of the First Occurrence in a String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/)

### Approach
Two-pointer approach: iterate through haystack, and for each position check if needle matches starting from that position using nested loop.

### Complexity
- **Time:** O(n*m) where n = len(haystack), m = len(needle)
- **Space:** O(1)

### Edge Cases
- Empty needle returns 0
- Needle longer than haystack returns -1
- Single character matches

### Solution
```python
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
```

---

## Problem 2: [Problem Title]
**LeetCode:** [Link](https://leetcode.com/problems/)

### Approach
*Add your approach here (2-3 lines)*

### Complexity
- **Time:** O()
- **Space:** O()

### Edge Cases
*Add edge cases you learned from here*

---

## Problem 3: [Problem Title]
**LeetCode:** [Link](https://leetcode.com/problems/)

### Approach
*Add your approach here (2-3 lines)*

### Complexity
- **Time:** O()
- **Space:** O()

### Edge Cases
*Add edge cases you learned from here*

---
