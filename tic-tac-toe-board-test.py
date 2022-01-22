
from tic_tac_toe import *

#computer AI test

def putMoves(board: TicTacToeBoard, lst, sym):
    for m in lst:
        board.putMove(m[0], m[1], sym)

        
board = TicTacToeBoard(3)
putMoves(board, [(0, 0), (1, 1)], 'O')
putMoves(board, [(0, 2)], 'X')
board.prnBoard()
#won, pos = winningMove(board, 'X')
#print(f"won = {won} pos = {pos}")
pos = computerMove(board, 'X')
print(f"pos = {pos}")

   
"""
#board building test
for i in range(1, 10):
    board = TicTacToeBoard(i)
    board.prnBoard()

"""











