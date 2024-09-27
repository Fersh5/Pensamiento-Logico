# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
# You must do it in place.

# Example 1:
# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]

# Example 2:
# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        index=[]
        axis_x=len(matrix)
        axis_y=len(matrix[0])
        for row in range(axis_x):
            for column in range(axis_y):
                if matrix[row][column]==0:
                    index.append([row,column])
        for pars in index:
            for element in range(axis_y):
                matrix[pars[0]][element]=0
            for element in range(axis_x):
                matrix[element][pars[1]]=0
        print(matrix)


case_1=Solution()
case_1.setZeroes([[1,1,1],[1,0,1],[1,1,1]])
case_1.setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]])
