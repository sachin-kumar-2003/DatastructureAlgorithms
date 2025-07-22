'''1791. Find Center of Star Graph'''
from collections import defaultdict
from typing import List
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        n=len(edges)+1
        adjList = defaultdict(list)
        for u,v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        
        for i in range(1,n+1):
            if len(adjList[i]) == n-1:
                return i
        return -1