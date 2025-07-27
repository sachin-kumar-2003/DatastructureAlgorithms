from heapq import heappush,heappop,heapify
from collections import Counter
from typing import List
class Solution:
    def maximumMedianSum(self, nums: List[int]) -> int:
        ans = 0
        freq = Counter(nums)
        maxH = [ -x for x in nums]
        heapify(maxH)
        heapify(nums)
        while freq:
            first = heappop(nums)
            second = -heappop(maxH)
            third = -heappop(maxH)
            freq[first] -= 1
            freq[second] -= 1
            freq[third] -= 1
            if freq[first]==0:del freq[first]
            if freq[second]==0:del freq[second]
            if freq[third] == 0:del freq[third]
            a=[ first, second , third]
            a.sort()
            ans += a[1]
        return ans