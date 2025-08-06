'''1443. Minimum Time to Collect All Apples in a Tree'''
from collections import defaultdict
from typing import List

class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adjList = defaultdict(list)

        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        def dfs(node, parent):
            total = 0
            for child in adjList[node]:
                if child == parent:
                    continue
                childTime = dfs(child, node)
                if childTime > 0 or hasApple[child]:
                    total += childTime + 2
            return total

        return dfs(0, -1)
