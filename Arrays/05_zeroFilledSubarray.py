# 2348. Number of Zero-Filled Subarrays
from typing  import List
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans = 0
        zero = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zero += 1
            else:
                ans += (zero * (zero + 1)) // 2
                zero = 0
        ans += (zero * (zero + 1)) // 2
        return ans