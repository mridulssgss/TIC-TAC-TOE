# Name: Mrityunjay Jha
# Date: 21-01-2022


class TicTacToeBoard:
    def __init__(self, board_size):
        self.board_size = board_size
        self._board = []
        for _ in range(self.board_size):
            self._board.append([' '] * self.board_size )
        
    def prnBoard(self):
        print("")
        print("")
        for i in range(self.board_size - 1):
            for j in range(self.board_size):
                print(self._board[i][j], end = "|")
            print("")
            print("---" * self.board_size)
        for j in range(self.board_size):
            print(self._board[-1][j], end = "|")
        print("")
        print("")

    def isLegal(self, i, j, move):
        return 0 <= i < self.board_size and 0 <= j < self.board_size and self._board[i][j] == ' '

    def putMove(self, i, j, move):
        if self.isLegal(i, j, move):
            self._board[i][j] = move
            return True
        else:
            return False

    def getMove(self, i, j):
        if 0 <= i < self.board_size and 0 <= j < self.board_size:
            return self._board[i][j]
        else:
            return ' '
    
    def _rowCheck(self, x, y):
        for j in range(self.board_size):
           if self._board[x][y] != self._board[x][j]:
               return False
        return True
    
    def _colCheck(self, x, y):
        for i in range(self.board_size):
            if self._board[x][y] != self._board[i][y]:
                return False
        return True
    
    def _firstDiagCheck(self, x, y):
        for i in range(1, self.board_size):
            if self._board[i][i] != self._board[0][0]: return False
        return True

    def _secondDiagCheck(self, x, y):
        for f in range(self.board_size):
            xd, yd = f, self.board_size - 1 - f
            if self._board[xd][yd] != self._board[0][-1]: return False
        return True

    def winningMove(self, x, y):
        if(self._board[x][y] == ' '): return False
        return self._rowCheck(x, y) or self._colCheck(x, y) or (x == y and self._firstDiagCheck(x, y)) or ((x == self.board_size - 1 - y) and self._secondDiagCheck(x, y))
    
    def removeMove(self, x, y):
        if 0 <= x < self.board_size and 0 <= y < self.board_size:
            self._board[x][y] = ' '

    
    
"""
board = TicTacToeBoard(3)
board.putMove(0, 0, 'X')
board.prnBoard()
board.putMove(1, 2, 'Y')
board.putMove(0, 1, 'X')
board.putMove(0, 2, 'X')

board.prnBoard()

if board.winningMove(0, 0):
    print("winner")
"""    

def oppPlayer(char):
    dict = {'X':'O', 'O':'X'}
    return dict[char] if char in dict else ' '

def rowNMinusOne(board: TicTacToeBoard, r, ch):
    vacant_pos = -1
    ch_reads = 0
    for j in range(board.board_size):
        if(board.getMove(r, j) == ' '):
            vacant_pos = j
        elif(board.getMove(r, j) == ch):
            ch_reads += 1
    if(ch_reads == board.board_size - 1):
        return (True, vacant_pos)
    else:
        return (False, vacant_pos)
    
def colNMinusOne(board, c, ch):
    vacant_pos = -1
    ch_reads = 0
    for i in range(board.board_size):
        if(board.getMove(i, c) == ' '):
            vacant_pos = i
        elif(board.getMove(i, c) == ch):
            ch_reads += 1
    if(ch_reads == board.board_size - 1):
        return (True, vacant_pos)
    else:
        return (False, vacant_pos)

def firstDiagNMinusOne(board: TicTacToeBoard, ch):
    vacant_pos = -1
    char_reads = 0
    for i in range(board.board_size):
        if(board.getMove(i, i) == ' '):
            vacant_pos = i
        elif(board.getMove(i, i) == ch):
            char_reads += 1
    if(char_reads == board.board_size - 1):
        return (True, (vacant_pos, vacant_pos))       
    else:
        return (False, (vacant_pos, vacant_pos))

def secondDiagMinusOne(board: TicTacToeBoard, ch):
    vacant_pos = -1
    char_reads = 0
    for f in range(board.board_size):
        r, c = f, board.board_size - 1 - f
        if(board.getMove(r, c) == ' '):
            vacant_pos = (r, c)
        elif(board.getMove(r, c) == ch):
            char_reads += 1
    if(char_reads == board.board_size - 1):
        return (True, vacant_pos)
    else:
        return (False, vacant_pos)

def diagNMinusOne(board: TicTacToeBoard, ch):
    won, pos = firstDiagNMinusOne(board, ch)
    if(won):  return won, pos
    won, pos = secondDiagMinusOne(board, ch)    
    return won, pos

def winningMove(board: TicTacToeBoard, ch):
    mx, my = -1, -1
    for r in range(board.board_size):
        wmv, c = rowNMinusOne(board, r, ch)
        if(wmv): return (r, c)
        if(c != -1 and mx == -1 and my == -1):
            mx, my = r, c

    for c in range(board.board_size):
        wmv, r = colNMinusOne(board, c, ch)
        if(wmv): return (r, c)
    
    won, move_pos = diagNMinusOne(board, ch)
    return move_pos if won else (mx, my)

def computerMove(board: TicTacToeBoard, move_char):
    "does move according to heuristic and changes state of board"
    op_player = oppPlayer(move_char)
    
    won, pos = winningMove(board, move_char)
    if(won): return pos

    won, pos = winningMove(board, op_player)
    return pos

def playerMove(board: TicTacToeBoard, move_char):
    x, y = [int(j) for j in input().split()]
    while(not board.isLegal(x, y, move_char)):
        print("Illegal Move Try Again")
        x, y = [int(j) for j in input().split()]
    return x, y

def play(board: TicTacToeBoard, player, sym1, opp, sym2):
    move = (0, 0)
    no_of_moves = 0
    max_moves = board.board_size * board.board_size

    while(no_of_moves < max_moves and not board.winningMove(move[0], move[1])):
        board.prnBoard()
        move = player(board, sym1)
        board.putMove(move[0], move[1], sym1)
        no_of_moves += 1
        
        if(board.winningMove(move[0], move[1])): break
        
        board.prnBoard()
        move = opp(board, sym2)
        board.putMove(move[0], move[1], sym2)
        no_of_moves += 1
    
    board.prnBoard()
    if(no_of_moves % 2):
        print("Player 1 wins")
    else:
        print("Player 2 wins")


play(TicTacToeBoard(3), playerMove, 'O', playerMove, 'X')

    

