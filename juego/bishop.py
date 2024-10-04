from juego.piece import Piece

class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)

    def valid_moves(self, current_position, board):
        return self._get_moves_in_directions(current_position, board, [
            (-1, -1), (-1, 1),  
            (1, -1), (1, 1)   
        ])

    def _get_moves_in_directions(self, current_position, board, directions):
        moves = []
        for dr, dc in directions:
            moves.extend(self._explore_direction(current_position, board, dr, dc))
        return moves

    def _explore_direction(self, current_position, board, dr, dc):
        """Explora una dirección específica para encontrar los movimientos válidos."""
        row, col = current_position
        new_row, new_col = row + dr, col + dc
        moves = []
        
        while self.is_within_bounds(new_row, new_col):
            if self.is_empty(board, new_row, new_col):
                moves.append((new_row, new_col))
            elif self.is_opponent_piece(board, new_row, new_col):
                moves.append((new_row, new_col))
                break
            else:
                break
            new_row += dr
            new_col += dc

        return moves

    def get_symbol(self):
        return "B" if self.get_color() == 'White' else "b"
