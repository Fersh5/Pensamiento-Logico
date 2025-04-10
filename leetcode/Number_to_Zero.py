# Given an integer array nums of size n, return the number with the value closest to 0 in nums. 
# If there are multiple answers, return the number with the largest value.

# Example 1:
# Input: nums = [-4,-2,1,4,8]
# Output: 1
# Explanation:
# The distance from -4 to 0 is |-4| = 4.
# The distance from -2 to 0 is |-2| = 2.
# The distance from 1 to 0 is |1| = 1.
# The distance from 4 to 0 is |4| = 4.
# The distance from 8 to 0 is |8| = 8.
# Thus, the closest number to 0 in the array is 1.

# Example 2:
# Input: nums = [2,-1,1]
# Output: 1
# Explanation: 1 and -1 are both the closest numbers to 0, so 1 being larger is returned.
from typing import List

class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        result = nums[0]
        if len(nums)==1:
            return result
        for num in range(1,len(nums)):
            if abs(result) == abs(nums[num]):
                if result != nums[num]:
                    result = abs(result)
            elif abs(nums[num])<abs(result):
                result = nums[num]
            if nums[num]==nums[-1]:
                return result
                

case_1= Solution()
print(case_1.findClosestNumber([-100000,-100000]))
            


                