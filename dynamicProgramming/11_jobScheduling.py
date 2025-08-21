# 1235. Maximum Profit in Job Scheduling
from typing import List
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        arr = [[a, b, c] for a, b, c in zip(startTime, endTime, profit)]
        arr.sort()
        n = len(arr)
        memo = [-1] *(n+1)
        def getIdx(arr, l, r, target):
            res = r + 1
            while l <= r:
                mid = l + (r - l) // 2
                if arr[mid][0] >= target:
                    res = mid
                    r = mid - 1
                else:
                    l = mid + 1
            return res

        def dp(idx):
            if idx >= n:
                return 0
            if memo[idx] != -1:
                return memo[idx]
            skip = dp(idx+1)
            nextIdx = getIdx(arr, idx+1, n-1, arr[idx][1])
            take = arr[idx][2] + dp(nextIdx)
            memo[idx] = max(take, skip)
            return memo[idx]
        
        return dp(0)