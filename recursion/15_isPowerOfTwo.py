'''231. Power of Two'''
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        def recursion(num):
            if num > n:
                return False
            if num == n:
                return True
            return recursion(num * 2)
        return recursion(1)