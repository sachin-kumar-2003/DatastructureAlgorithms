# 446. Arithmetic Slices II - Subsequence
from collections import defaultdict
from typing import List
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        
        n = len(nums)
        res = 0
        mp = [defaultdict(int) for _ in range(n)]
        
        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                cnt = mp[j][diff]
                res += cnt
                mp[i][diff] += cnt + 1
        return res