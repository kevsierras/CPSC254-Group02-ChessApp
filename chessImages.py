
import pygame as py

WIDTH = 400
HEIGHT = 400
DIMENSION = 8 # dimension of the chess board
SQ_SIZE = HEIGHT / DIMENSION

class ImageState(): 

  def getWidth(self):
    return 400


  def getHeight(self): 
    return 400


  def getDimension(self): 
    return 8


  def getSquareSize(self): 
    SQ = getHeight() / getDimension()
    return SQ


  def drawScreen(self): 
    return py.display.set_mode((400, 400))

  
  def screenColor(self): 
    return drawScreen().fill(py.Color("white"))
  
  '''
  Load images of chess pieces
  '''
  def loadImages():
      pieces = ['wp', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bq', 'bR', 'bN', 'bB', 'bK', 'bQ']
      # load pieces here
      # use for loop to load images onto pieces

  '''
  Responsible for the graphics of the current game state
  '''
  def drawGameState(screen, gameState):
      drawBoard(screen) # draw squares on the drawBoard

      # add in piece highlighting or move suggestions (later)

      # drawPieces(screen, gameState.board) # draw pieces on the squares

  '''
  Draw the squares on the board. Top left square is always white.
  '''
  def drawBoard(screen):
      colors = [py.Color("white"), py.Color("gray")]
      for row in range(getDimension()):
          for column in range(getDimension()):
              color = colors[((row+column) % 2)]
              py.draw.rect(screen, color, py.Rect(column*getSquareSize(), row*getSquareSize(), getSquareSize(), getSquareSize()))

  '''
  Draw the chess pieces on the board using current GameState.board
  '''
  def drawPieces(screen, board):
      pass
