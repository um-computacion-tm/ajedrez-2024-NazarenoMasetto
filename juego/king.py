from juego.piece import Piece

class King(Piece):
    def __init__(self, color):
        super().__init__(color)

    def valid_moves(self, current_position, board):
        row, col = current_position
        # Movimientos en todas direcciones (1 casilla)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        return self._get_valid_moves(row, col, directions, board)

    def get_symbol(self):
        return "K" if self.get_color() == 'White' else "k"

    def _get_valid_moves(self, row, col, directions, board):
        valid_moves = []
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if self._is_within_board(new_row, new_col) and self._can_move_to(new_row, new_col, board):
                valid_moves.append((new_row, new_col))
        return valid_moves

    def _is_within_board(self, row, col):
        return 0 <= row < 8 and 0 <= col < 8

    def _can_move_to(self, row, col, board):
        target_piece = board[row][col]
        return target_piece == " " or target_piece.get_color() != self.get_color()
