'''47. Permutations II'''
from typing import List
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def recursion(nums,arr,idx):
            if idx == len(nums):
                arr.add(tuple(nums))
                return 
            for i in range(idx,len(nums)):
                nums[i],nums[idx] = nums[idx],nums[i]
                recursion(nums,arr,idx+1)
                nums[i],nums[idx] = nums[idx],nums[i]
        arr=set()
        recursion(nums,arr,0)
        return list(tuple(arr))