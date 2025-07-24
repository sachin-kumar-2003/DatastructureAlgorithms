'''886. Possible Bipartition'''
from collections import deque,defaultdict
from typing import List
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        color = [-1]*(n+1)
        adjList = defaultdict(list)

        for u,v in dislikes:
            adjList[u].append(v)
            adjList[v].append(u)
        
        def bfs(adjList ,node ,color):
            que = deque()
            que.append(node)
            color[node] = 1

            while que:
                curr = que.popleft()
                for ngbr in adjList[curr]:
                    if color[curr] == color[ngbr]:
                        return False
                    if color[ngbr] == -1:
                        color[ngbr] = 1 - color[curr]
                        que.append(ngbr)
            return True
        
        for i in range(1,n+1):
            if color[i] == -1:
                if bfs(adjList ,i ,color) == False:
                    return False
        return True
        