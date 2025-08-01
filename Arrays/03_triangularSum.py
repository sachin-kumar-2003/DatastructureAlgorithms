'''2221. Find Triangular Sum of an Array'''
from typing import List
class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        temp = nums
        for i in range(1, n):
            tempArr = []
            for j in range(1, len(temp)):
                num = (temp[j-1] + temp[j]) % 10
                tempArr.append(num)
            temp = tempArr
        return temp[0]
