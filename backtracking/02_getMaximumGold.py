# 1219. Path with Maximum Gold
from typing import List
def dfs(i, j, grid, m, n):
    if i < 0 or i >= m or j < 0 or j >= n:
        return 0
    if grid[i][j] == 0:
        return 0
    curr = grid[i][j]
    grid[i][j] = 0
    
    maxGold = max(
        dfs(i+1, j, grid, m, n),
        dfs(i-1, j, grid, m, n),
        dfs(i, j+1, grid, m, n),
        dfs(i, j-1, grid, m, n)
    )
    grid[i][j] = curr
    return curr + maxGold
class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    ans = max(ans, dfs(i, j, grid, m, n))
        return ans