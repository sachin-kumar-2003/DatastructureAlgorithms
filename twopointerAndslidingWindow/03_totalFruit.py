'''904. Fruit Into Baskets'''
from collections import defaultdict
from typing import List
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        n = len(fruits)
        ans = 0
        curr = 0
        freq = defaultdict(int)
        i = 0
        for r in range(n):
            freq[fruits[r]] += 1
            curr += 1
            while len(freq) > 2:
                freq[fruits[i]] -= 1
                if freq[fruits[i]] == 0:
                    del freq[fruits[i]]
                i += 1
                curr -= 1
            ans = max( ans , curr)
        return ans
            

        