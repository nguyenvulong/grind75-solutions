"""
If target exists, then return its index. Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity.
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #try:
        #    return nums.index(target)
        #except:
        #    return -1
        
        l,r = 0, len(nums) - 1
        while l < r:
            mid = int((l+r)/2) 
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                l = mid + 1
                #l = mid may create endless loop
            else:
                r = mid -1
                #r = mid should work too
        if target == nums[l]:
            return l
        return -1
