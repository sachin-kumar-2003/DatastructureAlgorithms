from collections import deque
from typing import List
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        n = len(maze)
        m = len(maze[0])

        i,j = entrance[0],entrance[1]
        if maze[i][j] == '+':return -1

        que = deque()
        que.append((i,j,0))
        maze[i][j] = '+'

        while que:
            x,y,l = que.popleft()
            dire = [[-1,0],[1,0],[0,1],[0,-1]]
            for a,b in dire:
                newX = x + a
                newY = y + b
                if newX  < 0 or newX > n-1 or newY < 0 or newY > m-1 or maze[newX][newY] == '+':
                    continue
                elif maze[newX][newY] == '.' and ( newX == 0 or newX == n-1 or newY == 0 or newY == m-1):
                    return l+1
                else:
                    que.append((newX,newY,l+1))
                    maze[newX][newY] = '+'
        return -1
