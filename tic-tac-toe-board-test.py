from lib2to3.pgen2.tokenize import TokenError
from tic_tac_toe import *

#computer AI test
"""
def putMoves(board: TicTacToeBoard, lst, sym):
    for m in lst:
        board.putMove(m[0], m[1], sym)

        
board = TicTacToeBoard(3)
putMoves(board, [(0, 0), (2, 0), (2, 2)], 'O')
putMoves(board, [(0, 2), (1, 1)], 'X')
board.prnBoard()
won, pos = winningMove(board, 'X')
print(f"won = {won} pos = {pos}")
pos = computerMove(board, 'X')
print(f"pos = {pos}")
"""
   

#board building test

board = TicTacToeBoard(10)
board.prnBoard()











