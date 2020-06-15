""""
Given an array nums containing n + 1 integers where each 
integer is between 1 and n (inclusive), prove that at least one
duplicate number must exist. Assume that there is only 
one duplicate number, find the duplicate one.

Input: [1,3,4,2,2]
Output: 2

constraints:
You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.
"""
from typing import List

class Solution:
    # floyd's cycle detection algorithm
    def findDuplicate(self, nums: List[int]) -> int:
        slow_ptr = 0
        fast_ptr = 0
        
        while True:
            slow_ptr = nums[slow_ptr]
            fast_ptr = nums[nums[fast_ptr]]
            
            if slow_ptr == fast_ptr:
                break
            
        slow_ptr = 0
        while slow_ptr != fast_ptr:
            slow_ptr = nums[slow_ptr]
            fast_ptr = nums[fast_ptr]
            
        return slow_ptr