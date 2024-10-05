# You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. 
# Check if these points make a straight line in the XY plane.

# Example 1:
# Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
# Output: true

# Example 2:
# Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
# Output: false

from typing import List

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        point_1=coordinates[0]
        point_2=coordinates[1]
        num_m=(point_2[1]-point_1[1])
        denom_m=(point_2[0]-point_1[0])
        if num_m==0 or denom_m==0:
            m=0
        else:
            m=num_m/denom_m
        b=point_1[1]-m*point_1[0]
        if num_m==0:
            for x,y in coordinates:
                if y == point_1[1]:
                    continue
                else:
                    return False
        elif denom_m==0:
            for x,y in coordinates:
                if x == point_1[0]:
                    continue
                else:
                    return False            
        else:
            for x,y in coordinates[2:]:
                if y== m*x+b:
                    continue
                else:
                    return False
        return True
       
        
                        
case_1=Solution()
print(case_1.checkStraightLine([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]))
print(case_1.checkStraightLine([[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]))
print(case_1.checkStraightLine([[1,2],[1,3],[1,4],[1,5],[1,6],[6,7]]))
print(case_1.checkStraightLine([[-3,-2],[-1,-2],[2,-2],[-2,-2],[0,-2]]))
print(case_1.checkStraightLine([[1,2],[2,3],[3,5]]))
print(case_1.checkStraightLine([[1,1],[2,2],[2,0]]))
print(case_1.checkStraightLine([[0,1],[1,3],[-4,-7],[5,11]]))
print(case_1.checkStraightLine([[0,0],[0,1],[0,-1]]))
print(case_1.checkStraightLine([[0,0],[0,5],[5,0],[1337,0],[0,1337]]))