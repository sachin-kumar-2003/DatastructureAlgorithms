from typing import List
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        if n < 3:
            return 0
        nums.sort()
        for i in range(n - 1, 1, -1): 
            left = 0
            right = i - 1 

            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    ans += (right - left)
                    right -= 1 
                else:
                    left += 1
        
        return ans