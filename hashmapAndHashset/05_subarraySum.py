# 560. Subarray Sum Equals K
from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        prefixSum = [0] * len(nums)
        prefixSum[0] = nums[0]
        for i in range(1, len(nums)):
            prefixSum[i] = prefixSum[i - 1] + nums[i]
        hashMap = dict()
        for i in range(len(nums)):
            if prefixSum[i] == k:
                ans += 1
            diff = prefixSum[i] - k
            if diff in hashMap.keys():
                ans += hashMap[diff]
            if prefixSum[i] in hashMap:
                hashMap[prefixSum[i]] += 1
            else:
                hashMap[prefixSum[i]] = 1
        return ans
