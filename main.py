"""
This is our main driver file. It will be responsible for handling user input and current GameState object.
"""
import pygame as py
import chessEngine

# WIDTH and HEIGHT can be adjusted for testing purpose
WIDTH = 400
HEIGHT = 400
DIMENSION = 8 # dimension of the chess board
SQ_SIZE = HEIGHT / DIMENSION
IMAGES = {}

'''
Main driver, will handle user input
'''
def startGame(): 
    py.init()
    screen = py.display.set_mode((WIDTH, HEIGHT))
    # can add user interface with commands or a side interface to show moves (optional)
    clock = py.time.Clock()
    screen.fill(py.Color("white"))
    gameState = chessEngine.GameState()
    loadImages() # only do this once, before the while loop
    running = True
    while running:
        for e in py.event.get():
            # if you press the 'X' button it will quit out
            if e.type == py.QUIT:
                running = False

        drawGameState(screen, gameState)
        py.display.flip()

'''
Load images of chess pieces
'''
def loadImages():
    pieces = ['p', 'r', 'n', 'b', 'q', 'k', 'P', 'R', 'N', 'B', 'Q', 'K']
    # load pieces here
    for piece in pieces: 
      IMAGES[piece] = py.transform.scale(py.image.load("chess_pieces/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))
    

'''
Graphics driver
'''
def drawGameState(screen, gameState):
    drawBoard(screen) # draw squares on the drawBoard

    # add in piece highlighting or move suggestions (later)

    drawPieces(screen, gameState.board)

'''
Draw the squares on the board. Top left square is always white.
'''
def drawBoard(screen):
    colors = [py.Color("gray"), py.Color("black")]
    for row in range(DIMENSION):
        for column in range(DIMENSION):
            color = colors[((row+column) % 2)]
            py.draw.rect(screen, color, py.Rect(column*SQ_SIZE, row*SQ_SIZE, SQ_SIZE, SQ_SIZE))

'''
Draw the chess pieces on the board using current GameState.board
'''
def drawPieces(screen, board):
    for row in range(DIMENSION): 
      for column in range(DIMENSION): 
        piece = board[row][column]
        # not an empty space
        if piece != '-':
          screen.blit(IMAGES[piece], py.Rect(column*SQ_SIZE, row*SQ_SIZE, SQ_SIZE, SQ_SIZE))

def main():
    startGame()

if __name__ == "__main__":
    main()