"""
Runtime: 0ms
Beats: 100.00%

Memory: 12.40MB
Beats: 80.82%
"""

class Solution(object):
    def plusOne(self, digits):
        n = len(digits) - 1
        for i in range(n, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits