# 3195. Find the Minimum Area to Cover All Ones I
from typing import List
class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        minRow , maxRow = n , -1
        minCol , maxCol = m , -1

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    minRow = min(minRow, i)
                    maxRow = max(maxRow, i)
                    minCol = min(minCol, j)
                    maxCol = max(maxCol, j)
        if maxRow == -1:
            return 0
        return (maxRow - minRow + 1) * (maxCol - minCol + 1)