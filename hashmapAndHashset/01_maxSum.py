'''3487. Maximum Unique Subarray Sum After Deletion'''
from typing import List
class Solution:
    def maxSum(self, nums: List[int]) -> int:
        ans = set()
        maxElement = max(nums)
        for num in nums:
            if num <= 0:
                continue
            else:
                ans.add(num)
        return sum(ans) if  ans else maxElement
        