"""
Runtime: 0ms
Beats: 100.00%

Memory: 12.43MB
Beats: 70.12%
"""

class Solution(object):
    def lengthOfLastWord(self, s):
        s = s.rstrip()
        words = s.split(" ")
        return len(words[-1])
