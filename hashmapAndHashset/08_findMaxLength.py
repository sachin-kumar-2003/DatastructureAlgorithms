# 525. Contiguous Array
class Solution:
  def findMaxLength(self, nums: list[int]) -> int:
    ones = zero = res = 0
    hashMap = {}
    for idx, val in enumerate(nums):
        if val == 0:
            zero += 1
        else:
            ones += 1
        if ones - zero not in hashMap:
            hashMap[ones - zero] = idx
        if ones == zero:
            res = ones + zero
        else:
            res = max(res, idx - hashMap[ones - zero])
    return res