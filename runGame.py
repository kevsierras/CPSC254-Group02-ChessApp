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
        while running:
            for event in py.event.get():
                # if you press the 'X' button it will quit out
                if event.type == py.QUIT:
                    running = False
    
            self.drawGameState(screen, gameState)
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