from piece import Piece

class Knight(Piece):
    def valid_moves(self, position, board):
        row, col = position
        moves = [(row + 2, col + 1), (row + 2, col - 1), (row - 2, col + 1), (row - 2, col - 1),
                 (row + 1, col + 2), (row + 1, col - 2), (row - 1, col + 2), (row - 1, col - 2)]
        return [(r, c) for r, c in moves if 0 <= r < 8 and 0 <= c < 8]