# You are given two strings s and t.

# String t is generated by random shuffling string s and then add one more letter at a random position.

# Return the letter that was added to t.

 

# Example 1:

# Input: s = "abcd", t = "abcde"
# Output: "e"
# Explanation: 'e' is the letter that was added.
# Example 2:

# Input: s = "", t = "y"
# Output: "y"

# class Solution:
#     def findTheDifference(self, s: str, t: str) -> str:
#         char_t=list(t)
#         for char in iter(s):
#             if char in char_t:
#                 char_t.remove(char)
#         return char_t.pop()

# class Solution:
#     def findTheDifference(self, s: str, t: str) -> str:
#         if len(t) == len(set(t)):
#             return (set(t)-set(s)).pop()
#         else:
#             for char in list(t):
#                 if list(t).count(char) > list(s).count(char):
#                     return char
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for char in list(t):
            if list(t).count(char) > list(s).count(char):
                return char


case1 = Solution()
print(case1.findTheDifference('abcd','abcde'))
print(case1.findTheDifference('','y'))
print(case1.findTheDifference('aba','aabb'))


