'''808. Soup Servings'''
class Solution:
    def dp(self, A, B, memo):
        if A<= 0 and B <= 0:
            return 0.5
        if A <= 0:
            return 1
        if B <= 0:
            return 0
        if ( A , B) in memo:
            return memo[( A , B)]

        first = second = third = fourth = 0
        first = self.dp( A - 100 , B, memo)
        second = self.dp( A - 75 , B - 25, memo)
        third = self.dp( A - 50 , B - 50, memo )
        fourth = self.dp( A - 25 , B - 75, memo)
        memo[(A , B)] = ( first + second + third + fourth ) / 4
        return memo[( A , B)]

    def soupServings(self, n: int) -> float:
        if n > 4500:return 1
        A = n
        B = n
        memo = {}
        return self.dp(A , B , memo)