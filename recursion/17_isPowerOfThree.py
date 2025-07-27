'''326. Power of Three'''
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        def recursion(num):
            if num > n:
                return False
            if num == n:
                return True
            return recursion(num * 3)
        return recursion(1)          
        
        