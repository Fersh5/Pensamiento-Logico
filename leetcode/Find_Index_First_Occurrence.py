# Find the Index of the First Occurrence in a String
# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

# Example 1:

# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
# Example 2:

# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.
class Solution_1:
    def strStr(self, haystack: str, needle: str) -> int:
        try:      
            haystack.index(needle)
        except Exception as ValueError:
            return -1
        return haystack.index(needle)

class Solution_2:
    def strStr(self, haystack: str, needle: str) -> int:
        i=0
        while True:
            if needle == haystack[i:len(needle)+i]:
                return i
            if haystack[i:len(needle)+i] == haystack[-1::len(needle)]:
                return -1
            i+=1
            
        
case1= Solution_1()
print(case1.strStr('sadbutsad','sad'))
print(case1.strStr('leetcode','leeto'))
print(case1.strStr('hello','ll'))

case2= Solution_2()
print(case2.strStr('sadbutsad','sad'))
print(case2.strStr('leetcode','leeto'))
print(case2.strStr('hello','ll'))

