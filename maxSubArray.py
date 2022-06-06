"""
Given an integer array nums, find the contiguous subarray 
which has the largest sum and return its sum.
Thanks: Xoldorov_Javohir
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
        c = 0
        maxSum = float('-inf')
        for i in range(0, len(nums)):
            c = max(nums[i], c + nums[i])
            maxSum = max(maxSum, c)
        return maxSum
            
