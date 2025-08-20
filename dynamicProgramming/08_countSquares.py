# 1277. Count Square Submatrices with All Ones
from typing import List
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        memo = [ [-1]* (m+1) for _ in range(n+1)]
        def dp(i, j):
            if i >= n or j >= m:
                return 0
            if matrix[i][j] == 0:
                return 0
            if memo[i][j] != -1:
                return memo[i][j]
            right = dp(i, j+1)
            dia = dp(i+1, j+1)
            down = dp(i+1, j)
            memo[i][j] = 1 + min(right, dia, down)
            return memo[i][j]
        res = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 1:
                    res += dp(i, j)
        return res