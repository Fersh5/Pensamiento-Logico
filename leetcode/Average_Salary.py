# You are given an array of unique integers salary where salary[i] is the salary of the ith employee.
# Return the average salary of employees excluding the minimum and maximum salary. Answers within 10-5 
# of the actual answer will be accepted.

 

# Example 1:
# Input: salary = [4000,3000,1000,2000]
# Output: 2500.00000
# Explanation: Minimum salary and maximum salary are 1000 and 4000 respectively.
# Average salary excluding minimum and maximum salary is (2000+3000) / 2 = 2500

# Example 2:
# Input: salary = [1000,2000,3000]
# Output: 2000.00000
# Explanation: Minimum salary and maximum salary are 1000 and 3000 respectively.
# Average salary excluding minimum and maximum salary is (2000) / 1 = 2000

from typing import List

class Solution:
    def average(self, salary: List[int]) -> float:
        high=salary[0]
        small=salary[0]
        total=0
        for i in salary:
            if i > high:
                high=i
            if i<small:
                small=i
            total += i
        return (total-small-high)/(len(salary)-2)
    
case_1=Solution()
print(case_1.average([4000,3000,1000,2000]))