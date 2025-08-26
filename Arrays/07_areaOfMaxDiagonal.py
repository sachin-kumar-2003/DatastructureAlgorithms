# 3000. Maximum Area of Longest Diagonal Rectangle
import math
from typing import List
class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        ans = float('-inf')
        res = float('-inf')
        for idx in range(len(dimensions)):
            l , b = dimensions[idx]
            if ans < math.sqrt(l * l + b * b):
                ans =  math.sqrt(l * l + b * b)
                res = l * b 
            if ans == math.sqrt(l * l + b * b):
                res = max(res, l * b)
        return res