'''2106. Maximum Fruits Harvested After at Most K Steps'''
from typing import List

class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        n = len(fruits)
        maxFruits = 0
        left = 0
        total = 0

        for right in range(n):
            total += fruits[right][1]

            while left <= right and not self.canReach(fruits[left][0], fruits[right][0], startPos, k):
                total -= fruits[left][1]
                left += 1

            maxFruits = max(maxFruits, total)

        return maxFruits

    def canReach(self, leftPos, rightPos, startPos, k):
        
        dist = min(
            abs(startPos - leftPos) + abs(rightPos - leftPos),
            abs(startPos - rightPos) + abs(rightPos - leftPos)
        )
        return dist <= k
