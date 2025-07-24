'''1971. Find if Path Exists in Graph'''
from collections import defaultdict
from typing import List
class Solution:
    def dfs(self,adjList,curr,dest,visited):
        if curr == dest:
            return True
        visited.add(curr)

        for ngbr in adjList[curr]:
            if ngbr not in visited and self.dfs(adjList,ngbr,dest,visited):
                return True
        return False
        

    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        adjList = defaultdict(list)

        for u,v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        
        visited = set()
        if self.dfs(adjList,source,destination,visited):
            return True
        return False