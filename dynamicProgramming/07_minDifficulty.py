# 1335. Minimum Difficulty of a Job Schedule
from math import inf
from typing import List
class Solution:
    def dp(self, idx, n, jb, d, memo):
        if d == 1:
            maxElement = max(jb[idx:])
            return maxElement
        if memo[idx][d] != -1:
            return memo[idx][d]
        maxElement = float(-inf)
        ans = float('inf')
        for i in range(idx, n-d+1):
            maxElement = max(maxElement, jb[i])
            res = maxElement + self.dp(i+1, n, jb, d-1, memo)
            ans = min(ans , res)
        memo[idx][d] = ans
        return ans

    def minDifficulty(self, jb: List[int], d: int) -> int:
        n = len(jb)
        if n < d:return -1
        memo = [ [-1]*(d+1) for _ in range(n+1)]
        return self.dp(0, n, jb, d, memo)