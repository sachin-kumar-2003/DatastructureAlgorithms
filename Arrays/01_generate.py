'''118. Pascal's Triangle'''
from typing import List
class Solution:
  def generate(self, n: int) -> List[List[int]]:
    res=[[1]]
    for i in range(1,n):
      prev=res[-1]
      tempArr=[1]
      for j in range(1,i):
        temp=prev[j-1]+prev[j]
        tempArr.append(temp)
      tempArr.append(1)
      res.append(tempArr)
    return res