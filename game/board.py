from game.rook import *
from game.knight import *
from game.bishop import *
from game.queen import *
from game.king import *
from game.pawn import *
class Board:
    def __init__(self):
        self.__positions__ = [[None for _ in range(8)] for _ in range(8)]
        self.__board__ = []
    def setup_board(self):
        for col in range(8):
            self.__positions__[1][col] = Pawn("BLACK", position=(1, col))
            self.__positions__[6][col] = Pawn("WHITE", position=(6, col))
        self.__positions__[0][0] = Rook("BLACK")
        self.__positions__[0][7] = Rook("BLACK")
        self.__positions__[7][0] = Rook("WHITE")
        self.__positions__[7][7] = Rook("WHITE")
        self.__positions__[0][1] = Knight("BLACK")
        self.__positions__[0][6] = Knight("BLACK")
        self.__positions__[7][1] = Knight("WHITE")
        self.__positions__[7][6] = Knight("WHITE")
        self.__positions__[0][2] = Bishop("BLACK")
        self.__positions__[0][5] = Bishop("BLACK")
        self.__positions__[7][2] = Bishop("WHITE")
        self.__positions__[7][5] = Bishop("WHITE")
        self.__positions__[0][3] = Queen("BLACK")
        self.__positions__[7][3] = Queen("WHITE")
        self.__positions__[0][4] = King("BLACK")
        self.__positions__[7][4] = King("WHITE")
    def get_piece(self, row, col):
        return self.__positions__[row][col]
    def move_piece(self, from_row, from_col, to_row, to_col):
        piece = self.get_piece(from_row, from_col)
        if piece and piece.is_valid_move(self, from_row, from_col, to_row, to_col):
            self.__positions__[to_row][to_col] = piece
            self.__positions__[from_row][from_col] = None
        else: raise ValueError("Movimiento inválido")
    def show_board(self):
        # Devuelve una representación textual del tablero
        board_str = ""
        for row in self.__positions__:
            for piece in row:
                if piece is None:
                    board_str += ". "
                else:
                    board_str += piece.symbol + " "
            board_str += "\n"
        return board_str