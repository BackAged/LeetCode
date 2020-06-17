"""
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
"""
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hm = dict()
        
        for i in nums:
            if i in hm:
                return True
            hm[i] = 1
            
        return False