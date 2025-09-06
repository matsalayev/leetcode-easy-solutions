"""
Runtime: 2ms
Beats: 66.52%

Memory: 12.56MB
Beats: 58.15%
"""

class Solution(object):
    def isValid(self, s):
        stack = []
        mapping = {')': '(', ']': '[', '}': '{'}

        for char in s:
            if char in mapping:
                top = stack.pop() if stack else '#'
                if mapping[char] != top:
                    return False
            else:
                stack.append(char)

        return not stack