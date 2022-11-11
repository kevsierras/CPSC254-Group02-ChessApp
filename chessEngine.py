"""
GameState class will be responsible for storing all the information of the curret state of a chess game.
Rules and tutorials will also be held here.
"""

class GameState():
    def __init__(self):
        # board is in characters to for easy parsing
        # 8x8 list, each list has 2 characters
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
