# 174. Dungeon Game
from functools import lru_cache
from typing import List
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])

        @lru_cache(None)
        def dp(i, j):
            if i == m - 1 and j == n - 1:
                return max(1, 1 - dungeon[i][j])
            
            need = float('inf')
            if i + 1 < m:
                need = min(need, dp(i+1, j))
            if j + 1 < n:
                need = min(need, dp(i, j+1))
            
            return max(1, need - dungeon[i][j])

        return dp(0, 0)
