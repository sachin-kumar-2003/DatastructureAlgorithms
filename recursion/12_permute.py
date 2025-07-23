'''46. Permutations'''
from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def recursion(nums,start,n,res):
            if start == n:
                res.append(nums[:])
                return
            for i in range(start,n):
                nums[start],nums[i] = nums[i],nums[start]
                recursion(nums,start+1,n,res)
                nums[start],nums[i] = nums[i],nums[start]
        res=[]
        recursion(nums,0,len(nums),res)
        return res