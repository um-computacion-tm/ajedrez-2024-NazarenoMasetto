from juego.piece import Piece
class King(Piece):
    def __init__(self, color):
        super().__init__(color)

    def valid_moves(self, current_position, board):
        row, col = current_position
        king_moves = [
            (-1, 0), (1, 0), (0, -1), (0, 1),  # Vertical y horizontal
            (-1, -1), (-1, 1), (1, -1), (1, 1)  # Diagonales
        ]
        valid_moves = []
        for move in king_moves:
            new_row, new_col = row + move[0], col + move[1]
            if self._is_within_board(new_row, new_col, board):
                valid_moves.append((new_row, new_col))
        return valid_moves

    def get_symbol(self):
        return "K" if self.get_color() == 'White' else "k"

    def _is_within_board(self, row, col, board):
        return 0 <= row < len(board) and 0 <= col < len(board[0])