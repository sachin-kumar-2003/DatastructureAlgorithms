# 1248. Count Number of Nice Subarrays
from typing import List
from collections import defaultdict
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        mp = defaultdict(int)
        mp[0] = 1
        oddCnt = 0
        ans = 0
        for num in nums:
            if num % 2 == 1:
                oddCnt += 1
            mp[oddCnt] += 1
            if oddCnt - k in mp:
                ans += mp[oddCnt - k]
        return ans