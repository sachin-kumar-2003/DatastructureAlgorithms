# 1124. Longest Well-Performing Interval
from typing import List
class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        total = 0
        seen = {}
        ans = 0
        for idx, val in enumerate(hours):
            if val > 8:
                total += 1
            else:
                total -= 1
            if total not in seen:
                seen[total] = idx
            if total > 0:
                ans = idx + 1
            if total  -1 in seen:
                ans = max(ans, idx - seen[total - 1])
        return ans