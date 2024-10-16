from juego.piece import Piece

class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)

    def valid_moves(self, current_position, board):
        row, col = current_position
        directions = self._get_directions()
        valid_moves = []
        for direction in directions:
            valid_moves.extend(self._explore_direction(row, col, direction, board))
        return valid_moves

    def get_symbol(self):
        return "Q" if self.get_color() == 'White' else "q"

    def _get_directions(self):
        return [
            (-1, 0), (1, 0),  # Vertical
            (0, -1), (0, 1),  # Horizontal
            (-1, -1), (-1, 1), (1, -1), (1, 1)  # Diagonal
        ]

    def _explore_direction(self, row, col, direction, board):
        valid_moves = []
        dr, dc = direction
        for i in range(1, 8):
            new_row, new_col = row + dr * i, col + dc * i
            if self._is_within_board(new_row, new_col):
                if self._is_target_valid(new_row, new_col, board):
                    valid_moves.append((new_row, new_col))
                    if isinstance(board[new_row][new_col], Piece):  # Stop if it hits another piece
                        break
                else:
                    break  # Invalid target, stop exploring this direction
            else:
                break  # Out of bounds
        return valid_moves
