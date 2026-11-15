class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        right = len(s)

        for left in range(right):
            rotated = s[left:right] + s[:left]
            if rotated == goal:
                return True

        return False
