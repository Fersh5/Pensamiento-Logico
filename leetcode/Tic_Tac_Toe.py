# Tic-tac-toe is played by two players A and B on a 3 x 3 grid. The rules of Tic-Tac-Toe are:

# Players take turns placing characters into empty squares ' '.
# The first player A always places 'X' characters, while the second player B always places 'O' characters.
# 'X' and 'O' characters are always placed into empty squares, never on filled ones.
# The game ends when there are three of the same (non-empty) character filling any row, column, or diagonal.
# The game also ends if all squares are non-empty.
# No more moves can be played if the game is over.
# Given a 2D integer array moves where moves[i] = [rowi, coli] indicates that the ith move will be played 
# on grid[rowi][coli]. return the winner of the game if it exists (A or B). In case the game ends in a 
# draw return "Draw". If there are still movements to play return "Pending".

# You can assume that moves is valid (i.e., it follows the rules of Tic-Tac-Toe), the grid is initially empty, and A will play first.

# Example 1:
# Input: moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
# Output: "A"
# Explanation: A wins, they always play first.

# Example 2:
# Input: moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
# Output: "B"
# Explanation: B wins.

# Example 3:
# Input: moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
# Output: "Draw"
# Explanation: The game ends in a draw since there are no moves to make.

from typing import List

class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        if len(moves)<5:
            return 'Pending'
        x=[0,0,0]
        y=[0,0,0]
        win=[[[0,0],[1,1],[2,2]],[[0,2],[1,1],[2,0]]]
        if (len(moves)-1)%2==0: 
            player = 'A'
            inicio=0
        else:
            player='B'
            inicio=1
        for move in moves[inicio::2]:
            y[move[0]]+=1
            x[move[1]]+=1    
            if move in win[0]:
                win[0].remove(move)
            if move in win[1]:
                win[1].remove(move)

        if 3 in y or 3 in x or not win[0] or not win[1]:
            return player
        elif len(moves)<9:
            return 'Pending'
        else:
            return 'Draw'

case_1=Solution()
print(case_1.tictactoe([[0,0],[2,0],[1,1],[2,1],[2,2]]))
print(case_1.tictactoe([[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]))
print(case_1.tictactoe([[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]))
print(case_1.tictactoe([[2,0],[1,1],[0,2],[2,1],[1,2],[1,0],[0,0],[0,1]]))

