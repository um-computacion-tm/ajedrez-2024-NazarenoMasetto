from rook import Rook
from knight import Knight
from bishop import Bishop
from queen import Queen
from king import King
from pawn import Pawn
class Board:
    def _init_(self):
        self._positions_ = [[None for _ in range(8)] for _ in range(8)]
        self.setup_board()

    def setup_board(self):
        
        for col in range(8):
            self._positions_[1][col] = Pawn("BLACK", f"{col+1}", position=(1, col))
            self._positions_[6][col] = Pawn("WHITE", f"{col+1}", position=(6, col))

        
        self._positions_[0][0] = Rook("BLACK")
        self._positions_[0][7] = Rook("BLACK")
        self._positions_[7][0] = Rook("WHITE")
        self._positions_[7][7] = Rook("WHITE")

        
        self._positions_[0][1] = Knight("BLACK")
        self._positions_[0][6] = Knight("BLACK")
        self._positions_[7][1] = Knight("WHITE")
        self._positions_[7][6] = Knight("WHITE")

        
        self._positions_[0][2] = Bishop("BLACK")
        self._positions_[0][5] = Bishop("BLACK")
        self._positions_[7][2] = Bishop("WHITE")
        self._positions_[7][5] = Bishop("WHITE")

        
        self._positions_[0][3] = Queen("BLACK")
        self._positions_[7][3] = Queen("WHITE")

        
        self._positions_[0][4] = King("BLACK")
        self._positions_[7][4] = King("WHITE")

    def get_piece(self, row, col):
        
        return self._positions_[row][col]
    
    def move_piece(self, from_row, from_col, to_row, to_col):
        piece = self.get_piece(from_row, from_col)
        if piece and piece.is_valid_move(self, from_row, from_col, to_row, to_col):
            self._positions_[to_row][to_col] = piece
            self._positions_[from_row][from_col] = None 
            
        else: raise ValueError("Movimiento inválido")