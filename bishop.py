from piece import Piece 
class Bishop(Piece):
    def valid_moves(self, position, board):
        row, col = position
        moves = [(row + i, col + i) for i in range(-7, 8) if 0 <= row + i < 8 and 0 <= col + i < 8 and i != 0] + \
                [(row + i, col - i) for i in range(-7, 8) if 0 <= row + i < 8 and 0 <= col - i < 8 and i != 0]
        return moves