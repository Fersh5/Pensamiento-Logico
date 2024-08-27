# Example 1:

# Input: s = "abab"
# Output: true
# Explanation: It is the substring "ab" twice.
# Example 2:

# Input: s = "aba"
# Output: false
# Example 3:

# Input: s = "abcabcabcabc"
# Output: true
# Explanation: It is the substring "abc" four times or the substring "abcabc" twice.


# class Solution:
#     def repeatedSubstringPattern(self, s: str) -> bool:
#         d={}
#         for i in range(int(len(s)/2)):
#             d[i] = s[:i+1]
#             if s==int((len(s)/(i+1)))*d[i]:
#                 return True
#         return False

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        sub= s+s
        return s in sub[1:-1]
        
        
case_1=Solution()
print(case_1.repeatedSubstringPattern('ab'))
print(case_1.repeatedSubstringPattern('abab'))
print(case_1.repeatedSubstringPattern('aba'))
print(case_1.repeatedSubstringPattern('ababab'))
print(case_1.repeatedSubstringPattern('aabaaba'))
print(case_1.repeatedSubstringPattern('babbabbabbabbab'))

