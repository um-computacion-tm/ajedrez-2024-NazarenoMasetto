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

    def _get_valid_moves(self, row, col, moves, board, limit=1):
        valid_moves = []
        for dr, dc in moves:
            valid_moves.extend(self._explore_moves_in_direction(row, col, dr, dc, board, limit))
        return valid_moves

    def _explore_moves_in_direction(self, row, col, dr, dc, board, limit=1):
        """Explora las posiciones en el tablero en una dirección específica."""
        valid_moves = []
        for step in range(1, limit + 1):
            new_row, new_col = row + dr * step, col + dc * step
            if not self._is_within_board(new_row, new_col):
                break
            target_square = board[new_row][new_col]
            if target_square == " ":
                valid_moves.append((new_row, new_col))
            elif target_square.get_color() != self.get_color():
                valid_moves.append((new_row, new_col))
                break
            else:
                break
        return valid_moves

    def _is_within_board(self, row, col):
        return 0 <= row < 8 and 0 <= col < 8

    @staticmethod
    def get_moves(move_type):
        if move_type == 'knight':
            return [
                (2, 1), (2, -1), (-2, 1), (-2, -1),
                (1, 2), (1, -2), (-1, 2), (-1, -2)
            ]
        elif move_type == 'directions':
            return [
                (-1, 0), (1, 0),  # Vertical
                (0, -1), (0, 1),  # Horizontal
                (-1, -1), (-1, 1), (1, -1), (1, 1)  # Diagonal
            ]
        else:
            raise ValueError("Invalid move type provided")
