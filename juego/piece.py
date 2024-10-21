class Piece:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def _generate_linear_moves(self, current_position, board, directions):
        moves = []
        for direction in directions:
            moves.extend(self._explore_direction(current_position[0], current_position[1], direction, board))
        return moves

    def _explore_direction(self, row, col, direction, board):
        moves = []
        new_row, new_col = row + direction[0], col + direction[1]
        while self.is_within_bounds(new_row, new_col):
            if board[new_row][new_col] == " ":
                moves.append((new_row, new_col))
            elif board[new_row][new_col].get_color() != self.get_color():
                moves.append((new_row, new_col))
                break
            else:
                break
            new_row += direction[0]
            new_col += direction[1]
        return moves

    def is_within_bounds(self, row, col):
        return 0 <= row < 8 and 0 <= col < 8
