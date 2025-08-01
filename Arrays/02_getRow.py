'''119. Pascal's Triangle II'''
from typing import List
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res=[[1]]
        for i in range(1,rowIndex + 1):
            prev=res[-1]
            tempArr=[1]
            for j in range(1,i):
                temp=prev[j-1]+prev[j]
                tempArr.append(temp)
            tempArr.append(1)
            res.append(tempArr)
        return res[-1]