"""
Runtime: 0ms
Beats: 100.00%

Memory: 12.99MB
Beats: 90.39%
"""

class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        for i, n in enumerate(nums):
            m = target - n
            if m in seen:
                return seen[m], i
            seen[n] = i
        return None
