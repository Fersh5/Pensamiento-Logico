# Write a function that takes the binary representation of a positive integer and returns the number of 
# set bits
#  it has (also known as the Hamming weight).
# Example 1:
# Input: n = 11
# Output: 3
# Explanation:
# The input binary string 1011 has a total of three set bits.

# Example 2:
# Input: n = 128
# Output: 1
# Explanation:
# The input binary string 10000000 has a total of one set bit.

# Example 3:
# Input: n = 2147483645
# Output: 30
# Explanation:
# The input binary string 1111111111111111111111111111101 has a total of thirty set bits.

class Solution:
    def hammingWeight(self, n: int) -> int:
        weight = 0
        while n:
            if n % 2 == 1:
                weight+=1
            n //= 2
        return weight
    
num_1 = Solution()

print(num_1.hammingWeight(11))
print(num_1.hammingWeight(128))
print(num_1.hammingWeight(2147483645))