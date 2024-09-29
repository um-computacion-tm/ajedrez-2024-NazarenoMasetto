from piece import Piece

class Knight(Piece):
    # Movimientos del caballo
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
        row, col = current_position
        moves = []

        for dr, dc in self.knight_moves:
            new_row, new_col = row + dr, col + dc
            if self._is_valid_move(new_row, new_col, board):
                moves.append((new_row, new_col))

        return moves

    def _is_valid_move(self, new_row, new_col, board):
        """Verifica si un movimiento es válido."""
        return (self.is_within_bounds(new_row, new_col) and 
                (self.is_empty(board, new_row, new_col) or 
                 self.is_opponent_piece(board, new_row, new_col)))

    def get_symbol(self):
        return "N" if self.get_color() == 'White' else "n"
