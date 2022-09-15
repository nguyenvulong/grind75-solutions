"""
Given an integer array nums, move all 0's to the end of it while 
maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
Thanks: Yi_Z, top answer
"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        j always tries to index the first zero in the list
        when nums[i] swaps with nums[j], the relative order 
        of the non-zero elements is retained
        """
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0 and nums[j] == 0:
                nums[i], nums[j] = nums[j], nums[i]
            if nums[j] != 0:
                j = j + 1
        print(nums)
        
class Solution_short:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
                
        return nums
