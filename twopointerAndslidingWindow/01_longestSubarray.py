from typing import List
'''2419. Longest Subarray With Maximum Bitwise AND'''
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxElement = max(nums)
        ans = 0
        i = 0
        j = 1
        while i < len(nums):
            j = i + 1
            if nums[i] == maxElement:
                cnt = 1
                while j < len(nums):
                    if nums[j] == nums[i]:
                        cnt += 1
                        j+=1
                    else:
                        i = j
                        break
                ans = max(ans, cnt)
                if j == len(nums):break
            else:
                i += 1
            
        return ans

