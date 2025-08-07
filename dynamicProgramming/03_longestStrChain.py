'''1048. Longest String Chain'''
from typing import List
class Solution:
    def check ( self , bigStr , smallStr):
        if len(bigStr) - len(smallStr) != 1:return False
        for i in range(len(bigStr)):
            newStr = bigStr[:i] + bigStr[i+1:]
            if newStr == smallStr:return True
        return False

    def dp( self , idx , prev , n , words , memo):
        if idx >= n:
            return 0
        take = skip =0
        if memo[idx][prev+1] != -1:
            return memo[idx][prev+1]

        skip = self.dp( idx +1 , prev , n , words , memo)
        if prev == -1 or self.check( words[idx] , words[prev] ):
            take = self.dp( idx + 1 , idx , n ,words , memo) + 1
        memo[idx][prev+1] = max(take , skip)
        return max(take ,skip)
        
    def longestStrChain(self, words: List[str]) -> int:
        n = len(words)
        words.sort(key = len)
        memo = [ [ -1] * (n+1) for _ in range(n+1)]
        return self.dp( 0 , -1 , n , words , memo)