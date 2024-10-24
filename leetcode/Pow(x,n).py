# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

# Example 1:
# Input: x = 2.00000, n = 10
# Output: 1024.00000

# Example 2:
# Input: x = 2.10000, n = 3
# Output: 9.26100

# Example 3:
# Input: x = 2.00000, n = -2
# Output: 0.25000
# Explanation: 2-2 = 1/22 = 1/4 = 0.25

# class Solution:
#     def myPow(self, x: float, n: int) -> float:
#         x_n=1
#         if n<0:
#             for _ in range((n*-1)):
#                 x_n/=x
#         elif n>0:
#             for _ in range(n):
#                 x_n*=x
#         return x_n
    
# class Solution:
#     def myPow(self, x: float, n: int) -> float:
#         return x**n
    
class Solution:
    def myPow(self, x: float, n: int) -> float:
        carry=1
        if n==0:
            return 1
        elif n<0:
            factor=1/x
            n=-n
        else:
            factor=x
        while n>0:
            if n%2 == 1:
                carry*=factor
                n-=1
                if n==0:
                    return carry
            else:
                factor*=factor
                n/=2
            




case_1=Solution()
print(case_1.myPow(2,10))
print(case_1.myPow(2.1,3))
print(case_1.myPow(2,-2))
print(case_1.myPow(0.00001,2147483647))
print(case_1.myPow(.44528,0))
print(case_1.myPow(8.95371,-1))