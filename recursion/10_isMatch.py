class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def recursion(i,j):
            if j == len(p):
                return i == len(s)
            
            firstMatch = i < len(s) and (s[i] == p[j] or p[j] == '.')
            if j+1 < len(p) and p[j+1] == '*':
                return recursion(i,j+2) or (firstMatch and recursion(i+1,j))
            else:
                return recursion(i+1,j+1) and firstMatch
        
        return recursion(0,0)