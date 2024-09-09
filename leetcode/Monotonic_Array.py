# An array is monotonic if it is either monotone increasing or monotone decreasing.
# An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. 
# An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

# Given an integer array nums, return true if the given array is monotonic, or false otherwise.

# Example 1:
# Input: nums = [1,2,2,3]
# Output: true

# Example 2:
# Input: nums = [6,5,4,4]
# Output: true

# Example 3:
# Input: nums = [1,3,2]
# Output: false

from typing import List

# class Solution:
#     def isMonotonic(self, nums: List[int]) -> bool:
#         asc= True
#         desc= True
#         for num in range(1,len(nums)):
#             if nums[num]<=nums[num-1]:
#                 continue
#             else:
#                 asc=False
#         for num in range(1,len(nums)):
#             if nums[num]>=nums[num-1]:
#                 continue
#             else:
#                 desc=False
#         return (asc or desc)

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        asc= True
        desc= True
        for num in range(1,len(nums)):
            if nums[num]<nums[num-1]:
                asc = False
            if nums[num]>nums[num-1]:
                desc = False
        return (asc | desc) 

case_1=Solution()
print(case_1.isMonotonic([1,2,2,3]))
print(case_1.isMonotonic([6,5,4,4]))
print(case_1.isMonotonic([1,3,2]))