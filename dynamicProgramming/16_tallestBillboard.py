from typing import List
class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        n = len(rods)
        mp = {}
        def dp(i, diff):
            if i == n:
                if diff == 0:
                    return 0
                return float('-inf')
            if (i, diff) in mp:
                return mp[(i, diff)]
            nt = dp(i+1, diff)
            l = rods[i] + dp(i+1, diff + rods[i])
            r = rods[i] + dp(i+1, diff - rods[i])
            mp[(i, diff)] =  max(nt, l, r)
            return mp[(i, diff)]
        return dp(0, 0) // 2