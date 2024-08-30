from rook import Rook
from knight import Knight
from bishop import Bishop
from queen import Queen
from king import King
from pawn import Pawn

class Board:
    def _init_(self):
        self._positions_ = []
        for _ in range(8):
            col = []
            for _ in range(8):
                col.append(None)
            self._positions_.append(col)
        
        
        self._positions_[0][0] = Rook("BLACK")  
        self._positions_[0][1] = Knight("BLACK")  
        self._positions_[0][2] = Bishop("BLACK")  
        self._positions_[0][3] = Queen("BLACK")  
        self._positions_[0][4] = King("BLACK")  
        self._positions_[0][5] = Bishop("BLACK")  
        self._positions_[0][6] = Knight("BLACK")  
        self._positions_[0][7] = Rook("BLACK")  
        
        
        for i in range(8):
            self._positions_[1][i] = Pawn("BLACK")
        
        
        self._positions_[7][0] = Rook("WHITE")  
        self._positions_[7][1] = Knight("WHITE")  
        self._positions_[7][2] = Bishop("WHITE")  
        self._positions_[7][3] = Queen("WHITE")  
        self._positions_[7][4] = King("WHITE")  
        self._positions_[7][5] = Bishop("WHITE")  
        self._positions_[7][6] = Knight("WHITE") 
        self._positions_[7][7] = Rook("WHITE")  
        
        
        for i in range(8):
            self._positions_[6][i] = Pawn("WHITE")

    def _str_(self):
        board_str = ""
        for row in self._positions_:
            for cell in row:
                if cell is not None:
                    board_str += str(cell)
                else:
                    board_str += " "
            board_str += "\n"
        return board_str

    def get_piece(self, row, col):
        return self._positions_[row][col]