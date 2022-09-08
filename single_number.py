"""
Given a non-empty array of integers nums, every element appears twice except for one. 
Find that single one.
Thanks: top answer
"""

class Solution:
    def singleNumber_(self, nums: List[int]) -> int:
        
        # if len(nums) == 1:
        #     return nums[0]
        
        store = []
        for num in nums:
            if num in store:
                store.remove(num)
            else:
                store.append(num)
        return store[0]
    
    def singleNumber_XOR(self, nums: List[int]) -> int:
        
        # if len(nums) == 1:
        #     return nums[0]
        
        x = 0
        for num in nums:
            x = x ^ num
        return x
