# 1239. Maximum Length of a Concatenated String with Unique Characters
from typing import List
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        n = len(arr)
        temp = ""
        memo = {}
        def containDuplicate(str1, str2):
            unique = set()
            for ch in str1:
                if ch in unique:return True
                unique.add(ch)
            for ch in str2:
                if ch in unique:return True
                unique.add(ch)
            return False
        def dp(idx, temp, memo):
            if idx >= n:
                return len(temp)
            if (idx, temp) in memo:
                return memo[(idx, temp)]
            take = skip = 0
            if containDuplicate(arr[idx], temp):
                skip = dp(idx+1, temp, memo)
            else:
                skip = dp(idx+1, temp, memo)
                take = dp(idx+1, temp + arr[idx], memo)
            memo[(idx, temp)] = max(take, skip)
            return max(take, skip)
        return dp(0, temp, memo)