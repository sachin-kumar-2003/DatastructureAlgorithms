'''2411. Smallest Subarrays With Maximum Bitwise OR'''
from typing import List
class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        setBitIdx = [-1] * 32
        res = [-1]*n

        for i in range(n-1 , -1 , -1):
            endIdx = i
            for j in range(32):
                if not (nums[i] & (1 << j)):
                    if setBitIdx[j] != -1:
                        endIdx = max(endIdx , setBitIdx[j])
                else:
                    setBitIdx[j] = i
            res[i] =  endIdx - i + 1
        return res
