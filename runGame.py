"""
This is our main driver file. It will be responsible for handling user input and current GameState object.
"""
import pygame as py
import chessEngine
import globalVariables

# global variables
gVar = globalVariables

class RunChessGame(): 
  '''
  Main driver, will handle user input
  '''
  def startGame(self): 
      py.init()
      screen = py.display.set_mode((gVar.WIDTH, gVar.HEIGHT))
      # can add user interface with commands or a side interface to show moves (optional)
      clock = py.time.Clock()
      screen.fill(py.Color("white"))
      gameState = chessEngine.GameState()
      self.loadImages() # only do this once, before the while loop
      running = True
      squareSelected = () # keep track of the last click (tuple: (row, column))
      playerClicks = [] # keep track of layer clicks (two tuples: [(6, 4), (4, 4)])
      while running:
        for event in py.event.get():
            # if you press the 'X' button it will quit out
            if event.type == py.QUIT:
              running = False
            # when you click the left click
            elif event.type == py.MOUSEBUTTONDOWN: 
              location = py.mouse.get_pos() # relative position of the mouse
              column = location[0] // gVar.SQ_SIZE # double divide to round the number
              row = location[1] // gVar.SQ_SIZE
              if squareSelected == (row, column): # if the user clicked on the same square
                squareSelected = () # deselect choice, no need to set the same position twice
                playerClicks = [] # clear the players log
              else: 
                squareSelected = (row, column) # store player choice
                playerClicks.append(squareSelected) # append players 1st and 2nd choice

              # after the players 2nd click, move pieces to the next square
              if len(playerClicks) == 2: 
                # call move class
                move = chessEngine.MovePieces(playerClicks[0], playerClicks[1], gameState.board)
                print(move.chessNotations())
                gameState.makeAMove(move)
                squareSelected = () # reset the users clicks
                playerClicks = []
        self.drawGameState(screen, gameState)
        clock.tick(gVar.MAX_FPS)
        py.display.flip()

  '''
  Load images of chess pieces
  '''
  @staticmethod
  def loadImages():
      pieces = ['p', 'r', 'n', 'b', 'q', 'k', 'P', 'R', 'N', 'B', 'Q', 'K']
      # load pieces here
      for piece in pieces: 
        gVar.IMAGES[piece] = py.transform.scale(py.image.load("chess_pieces/" + piece + ".png"), (gVar.SQ_SIZE, gVar.SQ_SIZE))
      
  
  '''
  Graphics driver
  '''
  def drawGameState(self, screen, gameState):
      self.drawBoard(screen) # draw squares on the drawBoard
  
      # add in piece highlighting or move suggestions (later)
  
      self.drawPieces(screen, gameState.board)
  
  '''
  Draw the squares on the board. Top left square is always white.
  '''
  @staticmethod
  def drawBoard(screen):
      colors = [py.Color("gray"), py.Color("black")]
      for row in range(gVar.DIMENSION):
          for column in range(gVar.DIMENSION):
              color = colors[((row+column) % 2)]
              py.draw.rect(screen, color, py.Rect(column*gVar.SQ_SIZE, row*gVar.SQ_SIZE, gVar.SQ_SIZE, gVar.SQ_SIZE))
  
  '''
  Draw the chess pieces on the board using current GameState.board
  '''
  @staticmethod
  def drawPieces(screen, board):
      for row in range(gVar.DIMENSION): 
        for column in range(gVar.DIMENSION): 
          piece = board[row][column]
          # not an empty space
          if piece != '-':
            screen.blit(gVar.IMAGES[piece], py.Rect(column*gVar.SQ_SIZE, row*gVar.SQ_SIZE, gVar.SQ_SIZE, gVar.SQ_SIZE))