class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        total = sum(nums)
        ans = 0
        prefix = 0
        for num in nums:
            prefix += num
            if (abs(total - prefix) - prefix ) % 2 == 0:
                ans += 1
        return ans - 1 if ans != 0 else 0