# 1792. Maximum Average Pass Ratio
from heapq import heapify, heappop, heappush
from typing import List
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        maxHeap = []
        ans = 0
        for a, b in classes:
            gain = ((a + 1)/(b + 1)) - (a/b)
            maxHeap.append([ - gain, a, b])
        print(maxHeap)
        heapify(maxHeap)

        for _ in range(extraStudents):
            gain , a, b = heappop(maxHeap)
            a += 1
            b += 1
            newGain = ((a + 1)/ (b + 1)) - ((a / b))
            heappush(maxHeap, [-newGain, a, b])
        for _, a, b in maxHeap:
            ans += (a/b)
        return ans / len(classes)