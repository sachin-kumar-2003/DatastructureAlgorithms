# 1557. Minimum Number of Vertices to Reach All Nodes
from typing import List
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        inDegree = [0]* n
        for u,v in edges:
            inDegree[v] += 1
        
        ans = []
        for i in range(n):
            if inDegree[i] == 0:
                ans.append(i)
        return ans