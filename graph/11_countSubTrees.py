from collections import defaultdict
from typing import List
class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        count = [0] * 26
        res = [0] * n

        adjList = defaultdict( list )
        for u , v in edges:
            adjList[u].append( v )
            adjList[v].append( u )
        
        def dfs( curr , prev , count , res):
            lab = labels[curr]
            idx = ord(lab) - ord('a')
            before = count[idx] 
            
            
            for ngbr in adjList[curr]:
                if ngbr == prev:
                    continue
                dfs( ngbr , curr  , count , res)
            count[idx] += 1
            after = count[idx]
            res[curr] = after - before

        dfs( 0 , -1 , count , res )
        return res