"""
This is our main driver file. It will be responsible for handling user input and current GameState object.
"""
import pygame as py
import chessEngine

# WIDTH and HEIGHT are 512 to evenly show all the squares
WIDTH = 512
HEIGHT = 512
DIMENSION = 8 # dimension of the chess board
SQ_SIZE = HEIGHT // DIMENSION


'''
Load images of chess pieces
'''
def loadImages():
    pieces = ['wp', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bq', 'bR', 'bN', 'bB', 'bK', 'bQ']
    # load pieces here
    # use for loop to load images onto pieces

'''
The main driver for our code. This will handle user input
'''
def main():
    py.init()
    screen = py.display.set_mode((WIDTH, HEIGHT))
    # can add user interface with commands or a side interface to show moves (optional)
    clock = py.time.Clock()
    screen.fill(py.Color("white"))
    gameState = chessEngine.GameState()
    # loadImages() # only do this once, before the while loop
    running = True
    while running:
        for e in py.event.get():
            # if you press the 'X' button it will quit out
            if e.type == py.QUIT:
                running = False

        drawGameState(screen, gameState)
        py.display.flip()

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
    for row in range(DIMENSION):
        for column in range(DIMENSION):
            color = colors[((row+column) % 2)]
            py.draw.rect(screen, color, py.Rect(column*SQ_SIZE, row*SQ_SIZE, SQ_SIZE, SQ_SIZE))

'''
Draw the chess pieces on the board using current GameState.board
'''
def drawPieces(screen, board):
    pass


if __name__ == "__main__":
    main()
