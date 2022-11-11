"""
GameState class will be responsible for storing all the information of the curret state of a chess game.
Rules and tutorials will also be held here.
"""
import chessBoardNotation

class GameState():
  def __init__(self):
      # board is in characters for easy parsing
      # 8x8 list, each list has 1 characters
      # The lowercase represents the black pieces, uppercase are the white pieces
      # The 'R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R' represent the individual chess pieces
      # The '-' represent an empty space
      self.board = [
          ["r", "n", "b", "q", "k", "b", "n", "r"],
          ["p", "p", "p", "p", "p", "p", "p", "p"],
          ["-", "-", "-", "-", "-", "-", "-", "-"],
          ["-", "-", "-", "-", "-", "-", "-", "-"],
          ["-", "-", "-", "-", "-", "-", "-", "-"],
          ["-", "-", "-", "-", "-", "-", "-", "-"],
          ["P", "P", "P", "P", "P", "P", "P", "P"],
          ["R", "N", "B", "Q", "K", "B", "N", "R"]
      ]
      self.whiteToMove = True
      self.moveLog = []

  def makeAMove(self, move):
      self.board[move.startSquare[0]][move.startSquare[1]] = "-"
      self.board[move.endSquare[0]][move.endSquare[1]] = move.pieceMoved
      self.moveLog.append(move) # log the move for undo
      self.whiteToMove = not self.whiteToMove # swap players

class MovePieces():  
  def __init__(self, startSquare, endSquare, board):
    # startSquare (tuple) and endSquare (tuple) is passed to check whether the move is a valid move
    # passing the board also updates the game board
    self.startSquare = startSquare
    self.endSquare = endSquare
    # keep track if a piece has moved and captured
    # [0] is the row and [1] is the column
    self.pieceMoved = board[self.startSquare[0]][self.startSquare[1]]
    self.pieceCaptured = board[self.endSquare[0]][self.endSquare[1]]

  def chessNotations(self): 
    return self.rankFiles(self.startSquare[0], self.startSquare[1]) + self.rankFiles(self.endSquare[0], self.endSquare[1])

  def rankFiles(self, row, column):
    gm = chessBoardNotation
    return gm.columnsToFiles[column] + gm.rowsToRanks[row]
