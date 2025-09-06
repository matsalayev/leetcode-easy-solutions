"""
Runtime: 10ms
Beats: 47.18%

Memory: 12.40MB
Beats: 53.37%

"""

class Solution(object):
    def romanToInt(self, s):
        values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        prev = 0

        for ch in reversed(s):
            val = values[ch]
            if val < prev:
                total -= val
            else:
                total += val
            prev = val
        return total
