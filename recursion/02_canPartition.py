"416. Partition Equal Subset Sum"
from typing import List
class Solution:
    def recursion(self,idx,nums,size,target,curr,memo):
        if idx==size:
            return False
        if curr==target:return True
        if (idx,curr) in memo:return memo[(idx,curr)]
        first= self.recursion(idx+1,nums,size,target,curr+nums[idx],memo)
        second= self.recursion(idx+1,nums,size,target,curr,memo)
        memo[(idx,curr)]= first or second
        return memo[(idx,curr)]

    def canPartition(self, nums: List[int]) -> bool:
        total=sum(nums)
        if total%2==1:return False
        target=total//2
        memo={}
        return self.recursion(0,nums,len(nums),target,0,memo)