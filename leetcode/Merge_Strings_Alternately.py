# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, 
# starting with word1. If a string is longer than the other, append the additional letters onto the 
# end of the merged string.

# Return the merged string.

# Example 1:
# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r

# Example 2:
# Input: word1 = "ab", word2 = "pqrs"
# Output: "apbqrs"
# Explanation: Notice that as word2 is longer, "rs" is appended to the end.
# word1:  a   b 
# word2:    p   q   r   s
# merged: a p b q   r   s

# Example 3:
# Input: word1 = "abcd", word2 = "pq"
# Output: "apbqcd"
# Explanation: Notice that as word1 is longer, "cd" is appended to the end.
# word1:  a   b   c   d
# word2:    p   q 
# merged: a p b q c   d

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        solution=[]
        count=0
        while len(solution) < len(word1)+len(word2):
            if len(word1)> count:
                solution += word1[count]
            if len(word2)> count:
                solution +=word2[count]
            count+=1
        return ''.join(solution)

example1 = Solution()

print(example1.mergeAlternately('abc','pqr'))
print(example1.mergeAlternately('ab','pqrs'))
print(example1.mergeAlternately('abcd','pq'))
