"2260. Minimum Consecutive Cards to Pick Up"
from typing import List
from collections import defaultdict
class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        freq = defaultdict(list)
        for idx,num in enumerate(cards):
            freq[num].append(idx)
        ans = float('inf')
        for key , val in freq.items():
            if len(val) > 1:
                for i in range(1,len(val)):
                    ans = min( ans , val[i] - val[i-1])
        return -1 if ans == float('inf') else ans + 1