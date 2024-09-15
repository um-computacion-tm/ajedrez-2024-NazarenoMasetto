from piece import Piece

class Queen(Piece):
    def __init__(self, color, position=None):
        super().__init__(color, position)

    def symbol(self):
      
        return 'Q' if self.get_color() == "WHITE" else 'q'

    def is_valid_piece_move(self, board, from_row, from_col, to_row, to_col):
      
        """Comprobar si el movimiento es horizontal o vertical"""
        if from_row == to_row or from_col == to_col:
           
            if from_row == to_row:
                """Movimiento horizontal"""
                for col in range(min(from_col, to_col) + 1, max(from_col, to_col)):
                    if board[from_row][col] is not None:
                        return False
            else:
                """Movimiento vertical"""
                for row in range(min(from_row, to_row) + 1, max(from_row, to_row)):
                    if board[row][from_col] is not None:
                        return False
            return True

        """Comprobar si el movimiento es diagonal"""
       
        elif abs(from_row - to_row) == abs(from_col - to_col):
        
        """Comprobar si hay piezas en el camino"""
        row_step = 1 if to_row > from_row else -1
        col_step = 1 if to_col > from_col else -1
        for i in range(1, abs(from_row - to_row)):
                row = from_row + i * row_step
                col = from_col + i * col_step
                if board[row][col] is not None:
                    return False
        return True

        """Si no es horizontal, vertical ni diagonal, el movimiento no es válido"""
        return False
    