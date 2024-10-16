class Piece:
    def __init__(self, color):
        self.__color__ = color

    def get_color(self):
        return self.__color__

    def valid_moves(self, current_position, board):
        raise NotImplementedError("Must implement valid_moves in subclasses.")

    def get_symbol(self):
        raise NotImplementedError("Must implement get_symbol in subclasses.")

    def __str__(self):
        return self.get_symbol()

    def _get_valid_moves(self, row, col, moves, board):
        valid_moves = []
        for dr, dc in moves:
            new_row, new_col = row + dr, col + dc
            if self._is_within_board(new_row, new_col):
                target_square = board[new_row][new_col]
                if target_square == " " or target_square.get_color() != self.get_color():
                    valid_moves.append((new_row, new_col))
        return valid_moves

    def _is_within_board(self, row, col):
        return 0 <= row < 8 and 0 <= col < 8

    def _get_directions(self):
        """
        Define the directions available for movement. Can be overridden in subclasses.
        """
        return []
