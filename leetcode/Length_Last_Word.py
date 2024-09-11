# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal 
# substring
#  consisting of non-space characters only.

 

# Example 1:

# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.
# Example 2:

# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.
# Example 3:

# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lenght=0
        for char in s[::-1]:
            if lenght==0 and char ==' ':
                continue
            if char == ' ':
                return lenght
            else:
                lenght+=1
        return lenght

case_1=Solution()
print(case_1.lengthOfLastWord('luffy is still joyboy'))
print(case_1.lengthOfLastWord('   fly me   to   the moon  '))
print(case_1.lengthOfLastWord('a'))
print(case_1.lengthOfLastWord('a '))