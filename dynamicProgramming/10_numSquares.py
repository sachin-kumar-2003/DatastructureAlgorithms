# 279. Perfect Squares
import math
class Solution:
    def numSquares(self, n: int) -> int:
        memo = [-1] * (n+1)
        def dp(num):
            if num == 0:
                return 0
            if memo[num] != -1:
                return memo[num]
            res = float('inf')
            for i in range(1, int(math.sqrt(num))+1):
                ans = 1 + dp(num - ( i * i))
                res = min(ans, res)
            memo[num] = res
            return res
        return dp(n)