# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each 
# number sorted in non-decreasing order.

# Example 1:
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].

# Example 2:
# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]

from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squares= []
        negative=[]
        num=0
        while True:
            if num<len(nums):
                if nums[num]<0:
                    negative.append(nums[num]**2)
                    num+=1
                elif not negative:
                    squares.append(nums[num]**2)
                    num+=1
                else:
                    if negative[-1]<nums[num]**2:
                        squares.append(negative.pop())             
                    else:
                        squares.append(nums[num]**2)
                        num+=1
            if num == len(nums) and negative:
                squares.append(negative.pop())
            if len(squares)==len(nums):
                return squares

lista=[-5,-3,1,2]
case_1=Solution()
print(case_1.sortedSquares([-7,-3,2,3,11]))
print(case_1.sortedSquares([-4,-1,0,3,10]))
print(case_1.sortedSquares(lista))
