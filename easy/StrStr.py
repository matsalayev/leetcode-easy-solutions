"""
Runtime: 0ms
Beats: 100.00%

Memory: 12.45MB
Beats: 51.90%
"""

class Solution(object):
    def strStr(self, haystack, needle):
        n, m = len(haystack), len(needle)

        for i in range(n - m + 1):
            if haystack[i:i+m] == needle:
                return i
        return -1
