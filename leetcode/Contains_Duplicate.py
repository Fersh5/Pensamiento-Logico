# Given an integer array nums, return true if any value appears at least twice in the array, 
# and return false if every element is distinct.
# Example 1:
# Input: nums = [1,2,3,1]
# Output: true

# Example 2:
# Input: nums = [1,2,3,4]
# Output: false

# Example 3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

class Solution:
    def containsDuplicate(self, nums) -> bool:
        comp_set = set(nums)
        if len(comp_set)<len(nums):
            return True
        else:
            return False

case_1=Solution()
nums_1 = [1,2,3,1]
nums_2 = [1,2,3,4]
nums_3 = [1,1,1,3,3,4,3,2,4,2]

print(case_1.containsDuplicate(nums_1))
print(case_1.containsDuplicate(nums_2))
print(case_1.containsDuplicate(nums_3))