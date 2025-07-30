'''60. Permutation Sequence'''
from math import factorial
class Solution:
    def getPermutation(self, n: int, k: int) -> str:        
        nums = [str(i) for i in range(1 , n+1)]
        k -= 1
        def recursion( n , k):
            if n == 0:
                return ''
            fact = factorial(n - 1)
            idx = k // fact
            digit = nums[idx]
            nums.pop(idx)
            return digit + recursion( n - 1 , k % fact)
            
        
        return recursion(n, k)
