"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""
from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        size = len(nums)
        
        to_set = 0
        not_zero = 0

        for i in range(size):
            if nums[i] != 0:
                not_zero += 1
                nums[to_set] = nums[i]
                to_set += 1
        
        for i in range(not_zero, size):
            nums[i] = 0
                    