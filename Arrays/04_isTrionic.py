'''3637. Trionic Array I'''
class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        i = 0
        first = []
        second = []
        third = []
        increase = False
        decrease = False
        secondIncrease = False
        for j in range(i+1,len(nums)):
            if nums[j] <= nums[j-1]:
                first.append(nums[j-1])
                break
            increase = True
            i = j
            first.append(nums[j-1])

        for j in range(i+1,len(nums)):
            if nums[j] >= nums[j-1]:
                break
            i = j
            decrease = True
            second.append(nums[j])
        for j in range(i+1, len(nums)):
            if nums[j] <= nums[j-1]:
                break
            secondIncrease = True
            i = j
            third.append(nums[j])

        if not first or not second or not third:
            return False
        if not increase or not decrease or not secondIncrease:
            return False
        return nums == first + second + third        