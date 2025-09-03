# 974. Subarray Sums Divisible by K
from typing import List
from collections import defaultdict
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ans = 0
        n = len(nums)
        mp = defaultdict(int)
        mp[0] = 1
        total  = 0
        for i in range(n):
            total += nums[i]
            rem = total % k
            if rem in mp:
                ans += mp[rem]
            mp[rem] += 1
        return ans