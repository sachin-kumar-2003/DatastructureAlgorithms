'''44. Wildcard Matching'''
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        N = len(s)
        M = len(p)
        memo = [[-1] * (M + 1) for _ in range(N + 1)]

        def recursion(i , j):
            if j == len(p):
                return i == len(s)
            if memo[i][j] != -1:return memo[i][j]
            if p[j] == '*':
                ans = recursion( i , j + 1) or ( i < len(s) and recursion( i + 1, j ))
            else:  
                first = (i < len(s)) and ( s[i] == p[j] or p[j] == '?')
                ans = first and recursion( i + 1,j + 1)
            memo[i][j] = ans
            return ans
        return recursion( 0 , 0)