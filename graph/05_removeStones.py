from typing import List
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        
        def dfs(idx, visited):
            visited[idx] = True
            r, c = stones[idx]
            for i in range(len(stones)):
                if not visited[i]:
                    if stones[i][0] == r or stones[i][1] == c:
                        dfs(i, visited)
        
        n = len(stones)
        visited = [False] * n
        cnt = 0
        for i in range(n):
            if not visited[i]:
                cnt += 1
                dfs(i, visited)
        
        return n - cnt
