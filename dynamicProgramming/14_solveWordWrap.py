# This is geeks for geeks problem 
# problem link:
# https://www.geeksforgeeks.org/problems/word-wrap1646/1
class Solution:
    def solveWordWrap(self, arr, k):
        n = len(arr)
        memo = {}
        def dp(idx, space):
            if idx == n:
                return 0
            newSpaces = space + 1 + arr[idx]
            if (idx, space) in memo:
                return memo[(idx, space)]
            first = second = float('inf')
            if newSpaces <= k:
                first = dp(idx+1, newSpaces)
            second = dp(idx+1, arr[idx]) + (k - space) * (k - space)
            memo[(idx, space)] = min(first, second)
            return memo[(idx, space)]
        
        return dp(1, arr[0])