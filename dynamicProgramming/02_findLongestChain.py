'''646. Maximum Length of Pair Chain'''
from collections import List
class Solution:
    def dp(self , idx , prev , n , pairs , memo):
        if idx >=n:
            return 0
        take = skip = 0
        if (idx , prev) in memo:
            return memo[(idx , prev)]

        skip = self.dp(idx + 1 ,prev , n , pairs, memo)
        if prev == -1 or pairs[prev][1] < pairs[idx][0]:
            take = self.dp( idx +1 , idx , n , pairs , memo) + 1

        memo[(idx,prev)] = max(skip , take)
        return max(skip , take)
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        n = len(pairs)
        pairs.sort(key = lambda x:x[1])
        memo = {}
        return self.dp( 0 , -1 , n , pairs , memo )