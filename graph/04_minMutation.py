'''433. Minimum Genetic Mutation'''
from collections import deque
from typing import List
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bankMap={}
        for strg in bank:
            bankMap[strg]=1
        que=deque()
        visited=set()
        que.append(startGene)
        visited.add(startGene)
        level=0

        while que:
            n=len(que)
            for _ in range(n):
                curr=que.popleft()
                if curr == endGene:return level
                for ch in "ACGT":
                    for i in range(len(curr)):
                        ngbr=curr[:i]+ch+curr[i+1:]
                        if ngbr not in visited and ngbr in bankMap:
                            visited.add(ngbr)
                            que.append(ngbr)
            level+=1
        return -1