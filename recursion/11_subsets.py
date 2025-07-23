'''78. Subsets'''
from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def recursion(idx,res,curr):
            if idx == len(nums):
                res.append(curr[:])
                return 
            recursion(idx+1,res,curr)
            curr.append(nums[idx])
            recursion(idx+1,res,curr)
            curr.pop()
        res=[]
        recursion(0,res,[])
        return res