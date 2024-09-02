# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word
# or phrase, typically using all the original letters exactly once.

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False
#         word = list(t)
#         for char in s:
#             if char in word:
#                 word.remove(char)
#             else:
#                 return False
#         return True
    
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False
#         for char in s:
#             if s.count(char) != t.count(char):
#                 return False
#         return True

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         sl=list(s)
#         tl=list(t)
#         while True:
#             if sl[-1] in tl:
#                 tl.remove(sl[-1])
#                 sl.pop()
#             else:
#                 return False
#             if tl == sl:
#                 return True
#             elif tl==[] or sl == []:
#                 return False

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         sl=list(s)
#         tl=list(t)
#         while True:
#             if sl[-1]==tl[-1]:
#                 tl.pop()
#                 sl.pop()
#             elif sl[-1] in tl and tl[-1] in sl:
#                 tl.remove(sl[-1])
#                 sl.remove(tl[-1])
#                 sl.pop()
#                 tl.pop()
#             else:
#                 return False
#             if tl == sl:
#                 return True
#             elif tl==[] or sl == []:
#                 return False
            
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d_char= {}
        for char in s:
            if char in d_char:
                d_char[char] += 1
            else:
                d_char[char] = 1
        
        for char in t:
            if char not in d_char:
                return False
            elif d_char[char] != 1:
                d_char[char] -= 1
            else:
                d_char.pop(char)
        return len(d_char) == 0 
                    



case_1 = Solution()
print(case_1.isAnagram('anagram','nagaram'))
print(case_1.isAnagram('rat','car'))
print(case_1.isAnagram('a','a'))
