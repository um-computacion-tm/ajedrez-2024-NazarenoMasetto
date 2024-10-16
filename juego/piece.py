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
            valid_moves.extend(self._explore_moves(row, col, dr, dc, board))
        return valid_moves

    def _explore_moves(self, row, col, dr, dc, board, limit=1):
        """Explora las posiciones en el tablero en una dirección o un conjunto de direcciones."""
        valid_moves = []
        for step in range(1, limit + 1):  # Explora una cantidad limitada de pasos
            new_row, new_col = row + dr * step, col + dc * step
            if not self._is_within_board(new_row, new_col):
                break
            target_moves = self._evaluate_target(new_row, new_col, board)
            valid_moves.extend(target_moves)
            if target_moves and board[new_row][new_col] != " ":  # Si encuentra una pieza, detiene la exploración
                break
        return valid_moves

    def _evaluate_target(self, new_row, new_col, board):
        target_square = board[new_row][new_col]
        if target_square == " ":
            return [(new_row, new_col)]  # Movimiento vacío
        elif target_square.get_color() != self.get_color():
            return [(new_row, new_col)]  # Captura
        return []  # No se puede mover

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
