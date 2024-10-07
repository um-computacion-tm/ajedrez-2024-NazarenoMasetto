from juego.piece import Piece
class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)

    def valid_moves(self, current_position, board):
        row, col = current_position
        moves = []
        directions = self._get_standard_directions()

        for direction in directions:
            moves += self._get_moves_in_direction(row, col, board, direction)

        return moves

    def _get_moves_in_direction(self, row, col, board, direction):
        dr, dc = direction
        moves = []
        new_row, new_col = row + dr, col + dc

        while self._is_within_board(new_row, new_col):
            target_piece = board[new_row][new_col]
            if target_piece == " ":
                moves.append((new_row, new_col))
            elif target_piece.get_color() != self.get_color():
                moves.append((new_row, new_col))
                break
            else:
                break
            new_row += dr
            new_col += dc

        return moves

    def get_symbol(self):
        return "Q" if self.get_color() == 'White' else "q"



