'''2215. Find the Difference of Two Arrays'''
from typing import List
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans=[]
        set1=set(nums1)
        set2=set(nums2)
        ans.append(list(set1-set2))
        ans.append(list(set2-set1))
        return ans