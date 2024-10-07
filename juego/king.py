from juego.piece import Piece

class King(Piece):
    def __init__(self, color):
        super().__init__(color)

    def valid_moves(self, current_position, board):
        row, col = current_position
        moves = []
        directions = self._get_standard_directions()

        for direction in directions:
            new_row, new_col = row + direction[0], col + direction[1]
            if self._is_within_board(new_row, new_col):
                target_piece = board[new_row][new_col]
                if target_piece == " " or target_piece.get_color() != self.get_color():
                    moves.append((new_row, new_col))

        return moves

    def get_symbol(self):
        return "K" if self.get_color() == 'White' else "k"


