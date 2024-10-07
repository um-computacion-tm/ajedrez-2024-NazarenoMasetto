from juego.piece import Piece
class Knight(Piece):
    KNIGHT_MOVES = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

    def __init__(self, color):
        super().__init__(color)

    def valid_moves(self, current_position, board):
        row, col = current_position
        moves = []

        for move in Knight.KNIGHT_MOVES:
            new_row, new_col = row + move[0], col + move[1]
            if self._is_within_board(new_row, new_col):
                target_piece = board[new_row][new_col]
                if target_piece == " " or target_piece.get_color() != self.get_color():
                    moves.append((new_row, new_col))

        return moves

    def get_symbol(self):
        return "N" if self.get_color() == 'White' else "n"


