'''2044. Count Number of Maximum Bitwise-OR Subsets'''
from typing import List
class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        maxOr = 0
        for num in nums:
            maxOr = maxOr | num
        
        def backtrack(idx , nums , OR , ans , target):
            if idx == len(nums):
                return 1 if OR == target else 0

            take = backtrack(idx+1, nums , OR|nums[idx], ans , target)
            skip = backtrack(idx+1 , nums , OR , ans , target)

            return take + skip
        return backtrack(0 , nums , 0 , 0 , maxOr)
