# Given two binary strings a and b, return their sum as a binary string.

# Example 1:
# Input: a = "11", b = "1"
# Output: "100"

# Example 2:
# Input: a = "1010", b = "1011"
# Output: "10101"
 
# Constraints:
# 1 <= a.length, b.length <= 104
# a and b consist only of '0' or '1' characters.
# Each string does not contain leading zeros except for the zero itself.

# class Solution:
#     def addBinary(self, a: str, b: str) -> str:
#         return bin(int(a,2)+int(b,2))[2:]
    
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        in_a=len(a)-1
        in_b=len(b)-1
        carry=0
        result=[]
        while True:
            in_sum=int(a[in_a])+int(b[in_b])+carry
            if in_sum==0:
                result.append('0')
            elif in_sum==1:
                result.append('1')
                if carry==1:
                    carry=0
            elif in_sum==2:
                result.append('0')
                carry=1
            elif in_sum==3:
                result.append('1')
            if in_a == 0 and in_b==0 and carry==0:
                return "".join(result[::-1])
            if in_a==0:
                a='0'
            else:
                in_a-=1
            if in_b==0:
                b='0'
            else:
                in_b-=1
    
case_1=Solution()
print(case_1.addBinary('11','1'))
print(case_1.addBinary('1010','1011'))