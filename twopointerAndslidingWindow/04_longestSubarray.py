'''1493. Longest Subarray of 1's After Deleting One Element'''
from typing import List
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        skiped = False
        curr = ans = 0
        if(all(nums) == 1):
            return len(nums) -1
        for r, val in enumerate(nums):
            if val == 0 and  skiped:
                while left < r:
                    if nums[left] == 0:
                        left += 1
                        break
                    else:
                        curr -= 1
                    left += 1
            else:
                if val == 0: skiped = True
                else:
                    curr += 1
            ans = max(curr, ans)
        return ans
    