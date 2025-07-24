from collections import deque
from typing import List
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        keys = set()
        def dfs(curr,keys):
            keys.add(curr)
            for ngbr in rooms[curr]:
                if ngbr not in keys:
                    keys.add(ngbr)
                    dfs(ngbr,keys)

        dfs(0,keys)
        return len(keys) == len(rooms)        