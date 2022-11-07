"""
GameState class will be responsible for storing all the information of the curret state of a chess game.
Rules and tutorials will also be held here.
"""

class GameState():
    def __init__(self):
        # board is in characters to for easy parsing
        # 8x8 list, each list has 2 characters
        # The 'b' and 'w' represent the color
        # The 'R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R' represent the pieces
        # The '--' represent an empty space
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
        ]
        self.whiteToMove = True
        self.moveLog = []
