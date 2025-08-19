"2787. Ways to Express an Integer as Sum of Powers"
class Solution:
    def dp(self, num, n, x, memo):
        if n == 0:
            return 1
        if n < 0:
            return 0
        val = num ** x
        if val > n:
            return 0
        if memo[num][n] != -1:
            return memo[num][n]
        take = self.dp(num + 1, n - val, x, memo)
        skip = self.dp(num + 1 , n, x, memo)
        memo[num][n] = (take + skip) % (10 ** 9 + 7)
        return memo[num][n]
        
    def numberOfWays(self, n: int, x: int) -> int:
        memo = [[-1] * (301) for _ in range(301)]
        return self.dp(1, n, x, memo)