from piece import Piece

class King(Piece):
    def __init__(self, color, position=None):
        super().__init__(color, position)
        
    def symbol(self):
        return 'K' if self.get_color() == "WHITE" else 'k'
    
    def is_valid_piece_move(self, board, from_row, from_col, to_row, to_col):
        """Comprobar  si el movimiento del rey es valido"""
        
        return max(abs(from_row - to_row), abs(from_col - to_col)) == 1
    
   