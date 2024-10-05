# Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, formed from 
# three of these lengths. If it is impossible to form any triangle of a non-zero area, return 0.

# Example 1:
# Input: nums = [2,1,2]
# Output: 5
# Explanation: You can form a triangle with three side lengths: 1, 2, and 2.

# Example 2:
# Input: nums = [1,2,1,10]
# Output: 0
# Explanation: 
# You cannot use the side lengths 1, 1, and 2 to form a triangle.
# You cannot use the side lengths 1, 1, and 10 to form a triangle.
# You cannot use the side lengths 1, 2, and 10 to form a triangle.
# As we cannot use any three side lengths to form a triangle of non-zero area, we return 0.

from typing import List

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        triangle=[]
        triangle.append(nums.pop())
        triangle.append(nums.pop())
        triangle.append(nums.pop())
        if triangle[0]<triangle[1]+triangle[2]:
            return sum(triangle)
        else:
            i=0
            while nums:
                triangle[i]=nums.pop()
                if triangle[0]<triangle[1]+triangle[2] and triangle[1]<triangle[0]+triangle[2] and triangle[2]<triangle[1]+triangle[0]:
                    return sum(triangle)
                else:
                    i=(i+1)%3
            return 0
           

case_1=Solution()
print(case_1.largestPerimeter([2,1,2]))
print(case_1.largestPerimeter([1,2,1,10]))
print(case_1.largestPerimeter([1,2,2,4,18,8]))