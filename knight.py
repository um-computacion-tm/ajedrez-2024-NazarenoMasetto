from piece import Piece

class Knight(Piece):
    # Movimientos del caballo como atributo de clase
    knight_moves = [
        (2, 1), (2, -1),  
        (-2, 1), (-2, -1),  
        (1, 2), (1, -2),  
        (-1, 2), (-1, -2)
    ]

    def __init__(self, color):
        super().__init__(color)

    def valid_moves(self, current_position, board):
        """Genera los movimientos válidos del caballo."""
        moves = [self._get_new_position(current_position, dr, dc) for dr, dc in self.knight_moves]
        return [move for move in moves if self._is_valid_move(move, board)]

    def _get_new_position(self, current_position, dr, dc):
        """Calcula la nueva posición después de un movimiento."""
        row, col = current_position
        return (row + dr, col + dc)

    def _is_valid_move(self, position, board):
        """Verifica si un movimiento es válido."""
        new_row, new_col = position
        return (self.is_within_bounds(new_row, new_col) and 
                (self.is_empty(board, new_row, new_col) or 
                 self.is_opponent_piece(board, new_row, new_col)))

    def get_symbol(self):
        return "N" if self.get_color() == 'White' else "n"

