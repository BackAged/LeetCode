"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
"""
from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans = []
        
        carry = 0
        s = digits[len(digits)-1] + 1
        carry = s // 10
        
        ans.append(s % 10)
        
        for i in range(len(digits)-2, -1, -1):
            s = digits[i] + carry
    
            ans.append(s % 10)
            
            carry = s // 10
            
        
        if carry:
            ans.append(carry % 10)
            if carry // 10:
                ans.append(carry // 10)
        
        return ans[::-1]