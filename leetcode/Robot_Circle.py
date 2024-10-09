# On an infinite plane, a robot initially stands at (0, 0) and faces north. Note that:
# The robot can receive one of three instructions:

# "G": go straight 1 unit.
# "L": turn 90 degrees to the left (i.e., anti-clockwise direction).
# "R": turn 90 degrees to the right (i.e., clockwise direction).
# The robot performs the instructions given in order, and repeats them forever.

# Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.
# Example 1:
# Input: instructions = "GGLLGG"
# Output: true
# Explanation: The robot is initially at (0, 0) facing the north direction.
# "G": move one step. Position: (0, 1). Direction: North.
# "G": move one step. Position: (0, 2). Direction: North.
# "L": turn 90 degrees anti-clockwise. Position: (0, 2). Direction: West.
# "L": turn 90 degrees anti-clockwise. Position: (0, 2). Direction: South.
# "G": move one step. Position: (0, 1). Direction: South.
# "G": move one step. Position: (0, 0). Direction: South.
# Repeating the instructions, the robot goes into the cycle: (0, 0) --> (0, 1) --> (0, 2) --> (0, 1) --> (0, 0).
# Based on that, we return true.

# Example 2:
# Input: instructions = "GG"
# Output: false
# Explanation: The robot is initially at (0, 0) facing the north direction.
# "G": move one step. Position: (0, 1). Direction: North.
# "G": move one step. Position: (0, 2). Direction: North.
# Repeating the instructions, keeps advancing in the north direction and does not go into cycles.
# Based on that, we return false.

# Example 3:
# Input: instructions = "GL"
# Output: true
# Explanation: The robot is initially at (0, 0) facing the north direction.
# "G": move one step. Position: (0, 1). Direction: North.
# "L": turn 90 degrees anti-clockwise. Position: (0, 1). Direction: West.
# "G": move one step. Position: (-1, 1). Direction: West.
# "L": turn 90 degrees anti-clockwise. Position: (-1, 1). Direction: South.
# "G": move one step. Position: (-1, 0). Direction: South.
# "L": turn 90 degrees anti-clockwise. Position: (-1, 0). Direction: East.
# "G": move one step. Position: (0, 0). Direction: East.
# "L": turn 90 degrees anti-clockwise. Position: (0, 0). Direction: North.
# Repeating the instructions, the robot goes into the cycle: (0, 0) --> (0, 1) --> (-1, 1) --> (-1, 0) --> (0, 0).
# Based on that, we return true.

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        state=[0,0,0]
        coordinates=['n','w','s','e']
        moves={'n':1,'s':-1,'e':-1,'w':1}
        for move in instructions*4:
            if move == 'G':
                # print(state[0])
                if state[0] % 2 == 0:
                    state[2]+=moves[coordinates[state[0]]]
                else:
                    state[1]+=moves[coordinates[state[0]]]
            elif move == 'L':
                state[0]= (state[0]-1)%4
            else:
                state[0]= (state[0]+1)%4
            # print(state)
        return state[1:]==[0,0]

case_1=Solution()
print(case_1.isRobotBounded('GGLLGG')) 
print(case_1.isRobotBounded('GG'))
print(case_1.isRobotBounded('GL'))
print(case_1.isRobotBounded('LGLGGLGR'))
print(case_1.isRobotBounded('RLLGLRRRRGGRRRGLLRRR'))
print(case_1.isRobotBounded('GRGRGGRR'))