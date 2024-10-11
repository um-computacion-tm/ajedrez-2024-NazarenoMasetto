from juego.piece import Piece

class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)

    def valid_moves(self, current_position, board):
        row, col = current_position
        # Movimientos en forma de "L"
        knight_moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
        return self._get_valid_moves(row, col, knight_moves, board)

    def get_symbol(self):
        return "N" if self.get_color() == 'White' else "n"

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



