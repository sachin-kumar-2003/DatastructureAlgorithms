'''997. Find the Town Judge'''
from collections import defaultdict
from typing import List
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        adjList = defaultdict(list)
        trustSet=set()
        for a,b in trust:
            adjList[b].append(a)
            trustSet.add(a)
        
        for i in range(1,n+1):
            if i not in trustSet and len(adjList[i]) == n-1:
                return i
        
        return -1


