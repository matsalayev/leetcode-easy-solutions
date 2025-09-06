"""
Runtime: 16ms
Beats: 29.81%

Memory: 12.33MB
Beats: 81.22%
"""

class Solution(object):
    def isPalindrome(self, x):
        s = str(x)
        return s == s[::-1]
