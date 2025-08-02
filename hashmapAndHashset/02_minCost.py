'''2561. Rearranging Fruits'''
from collections import defaultdict
class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        
        minEle = float('inf')
        freq = defaultdict(int)
        for num in basket1:
            freq[num] += 1
        
        for num in basket2:
            freq[num] -= 1
        
        finalList = []
        for key , val in freq.items():
            minEle = min( minEle , key)
            if val == 0:
                continue
            if val % 2 == 1:return -1
            for _ in range(abs(val)//2):
                finalList.append(key)

        n = len(finalList)

        finalList.sort()
        finalList = finalList[:n//2]
        print(finalList)
        ans = 0
        for i in range(len(finalList)):
            ans += min( finalList[i] , minEle * 2)
        return ans