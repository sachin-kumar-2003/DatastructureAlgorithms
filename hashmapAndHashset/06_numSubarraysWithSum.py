# 930. Binary Subarrays With Sum
from typing import List
from collections import defaultdict
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        hashMap = defaultdict(int)
        hashMap[0] = 1
        ans = 0
        total = 0
        for i, val in enumerate(nums):
            total += val
            if total - goal in hashMap:
                ans += hashMap[total - goal]
                hashMap[total] += 1
            else:
                hashMap[total] += 1
        return ans
            
