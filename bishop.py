from piece import Piece

class Bishop(Piece):
    def __init__(self, color, position=None):
        super().__init__(color, position)
        
    def symbol(self):
        return 'B' if self.get_color() == "WHITE" else 'b'    
        
        
    def is_valid_move(self, board, from_row, from_col, to_row, to_col):
        
        if not super().is_valid_move(board, from_row, from_col, to_row, to_col):
         return False
        
        if abs(to_row - from_row) != abs(to_col - from_col):
            return False

       
        step = 1 if (to_row > from_row) == (to_col > from_col) else -1

       
        for i in range(1, abs(to_row - from_row)):
            row = from_row + i * (1 if to_row > from_row else -1)
            col = from_col + i * (1 if to_col > from_col else -1)
            if board.get_piece(row, col) is not None:
                return False

        if board.get_piece(to_row, to_col) is not None and board.get_piece(to_row, to_col).get_color() == self.get_color():
            return False

        return True