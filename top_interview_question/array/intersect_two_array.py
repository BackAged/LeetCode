"""
Given two arrays, write a function to compute their intersection.
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
"""
from typing import List

# with extra memory O(N + M)
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hm = dict()
        ans = []
        
        for v in nums1:
            if v in hm:
                hm[v] += 1
            else:
                hm[v] = 1
                
        for v in nums2:
            if v in hm and hm[v]:
                ans.append(v)
                hm[v] -= 1
        
        return ans

# without extra memory O(N + M)
class Solution1:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        ans = []

        nums1_index = 0
        nums2_index = 0

        while nums1_index < len(nums1) and nums2_index < len(nums2):
            if nums1[nums1_index] > nums2[nums2_index]:
                nums2_index += 1

            elif nums1[nums1_index] < nums2[nums2_index]:
                nums1_index += 1
            
            else:
                ans.append(nums1[nums1_index])
                nums1_index += 1
                nums2_index += 1
        
        return ans