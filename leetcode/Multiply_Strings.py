# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, 
# also represented as a string.

# Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

# Example 1:
# Input: num1 = "2", num2 = "3"
# Output: "6"

# Example 2:
# Input: num1 = "123", num2 = "456"
# Output: "56088"

# class Solution:
#     def multiply(self, num1: str, num2: str) -> str:
#         suma=0
#         cont_1=0
#         dif=ord('0')
#         for char in num1[::-1]:
#             cont_0=0
#             for char2 in num2[::-1]:
#                 suma+=(ord(char)-dif)*(ord(char2)-dif)*(10**cont_0)*(10**cont_1)
#                 cont_0+=1
#             cont_1+=1
#         return str(suma)

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        dif=ord('0')
        n1=0
        n2=0
        cont=0
        for char in num1[::-1]:
            n1+=(ord(char)-dif)*(10**cont)
            cont+=1
        cont=0
        for char in num2[::-1]:
            n2+=(ord(char)-dif)*(10**cont)
            cont+=1
        return str(n1*n2)

case_1=Solution()
print(case_1.multiply("123","456"))
