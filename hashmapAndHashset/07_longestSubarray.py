# https://www.geeksforgeeks.org/problems/longest-sub-array-with-sum-k0809/1
class Solution:
    def longestSubarray(self, arr, k):  
        ans = 0
        hashMap = {}
        total = 0
        for idx, val in enumerate(arr):
            total += val
            if total - k == 0:
                ans = max(ans, idx + 1)
            elif total - k in hashMap:
                ans = max(ans, idx - hashMap[total - k])
            if total not in hashMap:
                hashMap[total] = idx
        return ans