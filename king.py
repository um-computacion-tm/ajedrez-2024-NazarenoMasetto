class King:
    
    def valid_moves(self, position, board):
        row, col = position
        moves = [(row + i, col + j) for i in [-1, 0, 1] for j in [-1, 0, 1] if (i, j) != (0, 0)]
        return [(r, c) for r, c in moves if 0 <= r < 8 and 0 <= c < 8]

   