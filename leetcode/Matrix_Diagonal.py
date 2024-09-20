# Given a square matrix mat, return the sum of the matrix diagonals.
# Only include the sum of all the elements on the primary diagonal and all the elements on the 
# secondary diagonal that are not part of the primary diagonal.

# Example 1:

# Input: mat = [[1,2,3],
#               [4,5,6],
#               [7,8,9]]
# Output: 25
# Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
# Notice that element mat[1][1] = 5 is counted only once.

# Example 2:
# Input: mat = [[1,1,1,1],
#               [1,1,1,1],
#               [1,1,1,1],
#               [1,1,1,1]]
# Output: 8

# Example 3:
# Input: mat = [[5]]
# Output: 5

from typing import List

# class Solution:
#     def diagonalSum(self, mat: List[List[int]]) -> int:
#         asc=0
#         desc=len(mat)-1
#         diag=0
#         while asc < len(mat):
#             if asc==desc:
#                 diag+=mat[asc][asc]
#             else:
#                 diag+=mat[asc][asc]
#                 diag+=mat[asc][desc]
#             asc+=1
#             desc-=1
#         return diag
    
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        diag=0
        dim=len(mat)
        for i in range(dim):
            diag+=mat[i][i] + mat[i][dim-1-i]
        if dim%2==0:
            return diag
        else:
            diag-=mat[dim//2][dim//2]
            return diag
               
           


case_1=Solution()

print(case_1.diagonalSum([[1,2,3],[4,5,6],[7,8,9]]))
print(case_1.diagonalSum([[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]))