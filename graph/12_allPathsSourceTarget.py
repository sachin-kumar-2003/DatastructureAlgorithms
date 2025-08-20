# 797. All Paths From Source to Target
from typing import List
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        ans = []
        def dfs(node, temp):
            if node == n - 1:
                print(temp)
                ans.append(temp[:])
                return 
            for ngbr in graph[node]:
                dfs(ngbr, temp+[ngbr])
        
        dfs(0, [0])
        return ans