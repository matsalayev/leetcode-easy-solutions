"""
Runtime: 0ms
Beats: 100.00%

Memory: 12.34MB
Beats: 80.21%
"""

class Solution(object):
    def removeElement(self, nums, val):
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i
