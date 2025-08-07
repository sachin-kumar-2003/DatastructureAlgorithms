from typing import List
class Solution:
    def dp(self, idx , nums , n , memo , isEven):
        if idx == n:
            return 0
        if memo[isEven][idx] != -1:
            return memo[isEven][idx]
        skip = self.dp(idx+1 , nums , n , memo , isEven)
        val = nums[idx]
        if not isEven:
            val = -val
        take = self.dp(idx+1 , nums , n , memo , not isEven) + val
        memo[isEven][idx] = max(take , skip)
        return memo[isEven][idx]

    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [ [-1] * (n+1) for _ in range(2)]
        return self.dp( 0 , nums , n , memo , True)