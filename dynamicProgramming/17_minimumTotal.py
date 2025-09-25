from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        hm = {}
        def dfs(i, j):
            if i == n:
                return 0
            if (i, j) in hm:
                return hm[(i, j)]
            first = triangle[i][j] + dfs(i+1, j)
            second = triangle[i][j] + dfs(i+1, j+1)

            hm[(i, j)] = min(first, second)
            return hm[(i, j)]
        return dfs(0, 0)
            