from juego.piece import Piece
class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)

    def get_symbol(self):
        return 'N'

    def valid_moves(self, current_position, board):
        possible_moves = self._get_knight_moves()
        valid_moves = []

        for move in possible_moves:
            new_row, new_col = self._calculate_new_position(current_position, move)
            if self._is_within_board(new_row, new_col) and self._can_move_to(new_row, new_col, board):
                valid_moves.append((new_row, new_col))

        return valid_moves

    @staticmethod
    def _get_knight_moves():
        return [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

    def _can_move_to(self, row, col, board):
        target_piece = board[row][col]
        return target_piece is None or target_piece.get_color() != self.get_color()
