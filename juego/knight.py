from juego.piece import Piece
class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)

    def valid_moves(self, current_position, board):
        row, col = current_position
        knight_moves = [
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)
        ]
        valid_moves = []
        for move in knight_moves:
            new_row, new_col = row + move[0], col + move[1]
            if self._is_within_board(new_row, new_col, board):
                valid_moves.append((new_row, new_col))
        return valid_moves

    def get_symbol(self):
        return "N" if self.get_color() == 'White' else "n"

    def _is_within_board(self, row, col, board):
        return 0 <= row < len(board) and 0 <= col < len(board[0])