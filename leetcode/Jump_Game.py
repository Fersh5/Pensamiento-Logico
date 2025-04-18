# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
# Return true if you can reach the last index, or false otherwise.

# Example 1:
# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

# Example 2:
# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
 
from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        prev_point = nums[0]
        length_array = len(nums)
        for num in range(length_array):
            if prev_point < nums[num]:
                prev_point = nums[num]
            if num == length_array-1 or prev_point+num >= length_array:
                return True
            prev_point-=1
            if prev_point < 0:
                return False

case_1 = Solution()
print(case_1.canJump([2,3,1,1,4])) # True
print(case_1.canJump([3,2,1,0,4])) # False
print(case_1.canJump([1,0,1,0])) # False
print(case_1.canJump([0])) # True