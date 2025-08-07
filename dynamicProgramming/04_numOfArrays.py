'''1420. Build Array Where You Can Find The Maximum Exactly K Comparisons'''
class Solution:
    def __init__(self):
        self.mod = 10**9 + 7

    def dp(self, idx, N, M, maxVal, K, cost, memo):
        if idx == N:
            if cost == K:
                return 1
            return 0
        if (idx, maxVal, cost) in memo:
            return memo[(idx, maxVal, cost)]
        res = 0
        for i in range(1, M + 1):
            if i > maxVal:
                res += self.dp(idx + 1, N, M, i, K, cost + 1, memo)
            else:
                res += self.dp(idx + 1, N, M, maxVal, K, cost, memo)
        memo[(idx, maxVal, cost)] = res % self.mod
        return memo[(idx, maxVal, cost)]

    def numOfArrays(self, n: int, m: int, k: int) -> int:
    
        memo = {}
        return self.dp(0, n, m, 0, k, 0, memo)
