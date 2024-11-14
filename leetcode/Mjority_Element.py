# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element 
# always exists in the array.

# Example 1:
# Input: nums = [3,2,3]
# Output: 3

# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

from typing import List

# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         count={}
#         for i in nums:
#             if i in count:
#                 count[i]+=1
#             else:
#                 count[i]=1
#         moda=0
#         for num,times in count.items():
#             if times > moda:
#                 moda= times
#                 result = num
#         return result

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        probable=nums[0]
        count=0
        for i in nums:
            if count==0:
                probable=i
                count+=1
            elif i == probable:
                count+=1
            else: count-=1
        return probable






case_1=Solution()
print(case_1.majorityElement([1]))
print(case_1.majorityElement([2,2,1,1,1,2,2]))