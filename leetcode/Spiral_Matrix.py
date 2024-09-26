# Given an m x n matrix, return all elements of the matrix in spiral order.

# Example 1:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]

# Example 2:
# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]

from typing import List

# class Solution:
#     def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
#         spiral=[]
#         sup_x=len(matrix)
#         sup_y=len(matrix[0]) 
#         inf_x,inf_y=0,-1
#         x,y=0,0
#         while len(spiral)<(len(matrix)*len(matrix[0])):
#             if x==inf_x and y<sup_y:
#                 spiral.append(matrix[x][y])
#                 y+=1
#                 if y == sup_y:
#                     x+=1
#                     inf_x+=1
#             if y==sup_y-1 and x<sup_x:
#                 spiral.append(matrix[x][y])
#                 x+=1
#                 if x==sup_x:
#                     y-=1
#                     sup_y-=1
#             if x==sup_x-1 and y>inf_y:
#                 spiral.append(matrix[x][y])
#                 y-=1
#                 if y==inf_y:
#                     y+=1
#                     sup_x-=1
#                     x-=1
#             if y==inf_y+1 and x>inf_x-1:
#                 spiral.append(matrix[x][y])
#                 x-=1
#                 if x==inf_x:
#                     x+=1
#                     y+=1
#                     inf_y+=1            
#         return spiral

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        spiral=[]
        top_x=len(matrix)
        top_y=len(matrix[0])
        botton_x,botton_y,x,y=0,0,0,0
        while True:
            for element in range(botton_y,top_y):
                spiral.append(matrix[x][element])
                if element==top_y-1:
                    botton_x+=1
                    y=top_y-1

            if len(spiral)==len(matrix)*len(matrix[0]):
                return spiral
            
            for element in range(botton_x,top_x):
                spiral.append(matrix[element][y])
                if element==top_x-1:
                    top_y-=1
                    x=top_x-1
            
            if len(spiral)==len(matrix)*len(matrix[0]):
                return spiral

            for element in range(top_y-1,botton_y-1,-1):
                spiral.append(matrix[x][element])
                if element==botton_y:
                    top_x-=1
                    y=botton_y

            if len(spiral)==len(matrix)*len(matrix[0]):
                return spiral
            
            for element in range(top_x-1,botton_x-1,-1):
                spiral.append(matrix[element][y])
                if element==botton_x:
                    botton_y+=1
                    x=botton_x
                    y+=1

            if len(spiral)==len(matrix)*len(matrix[0]):
                return spiral                 
    

case_1=Solution()

print(case_1.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
print(case_1.spiralOrder([[2,3]]))

