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
                if self._is_target_valid(target_square):
                    valid_moves.append((new_row, new_col))
        return valid_moves

    def _is_target_valid(self, target_square):
        return target_square == " " or target_square.get_color() != self.get_color()

    def _is_within_board(self, row, col):
        return 0 <= row < 8 and 0 <= col < 8

    def _explore_direction(self, row, col, direction, board):
        valid_moves = []
        dr, dc = direction
        for step in range(1, 8):
            new_row, new_col = row + dr * step, col + dc * step
            if not self._is_within_board(new_row, new_col):
                break
            valid_moves.extend(self._check_target(new_row, new_col, board))
        return valid_moves

    def _check_target(self, new_row, new_col, board):
        target_square = board[new_row][new_col]
        if self._is_target_valid(target_square):
            if target_square == " ":
                return [(new_row, new_col)]
            else:
                return [(new_row, new_col)]  # Captura
        return []  # No se puede mover

    @staticmethod
    def get_knight_moves():
        return [
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)
        ]

    @staticmethod
    def get_directions():
        return [
            (-1, 0), (1, 0),  # Vertical
            (0, -1), (0, 1),  # Horizontal
            (-1, -1), (-1, 1), (1, -1), (1, 1)  # Diagonal
        ]
