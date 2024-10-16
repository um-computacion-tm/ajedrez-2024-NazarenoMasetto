from positions import Position
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

    def _get_valid_moves(self, pos, moves, limit=1):
        valid_moves = []
        for dr, dc in moves:
            valid_moves.extend(self._explore_moves_in_direction(pos, dr, dc, limit))
        return valid_moves

    def _explore_moves_in_direction(self, pos, dr, dc, limit=1):
        """Explora las posiciones en el tablero en una dirección específica."""
        valid_moves = []
        for step in range(1, limit + 1):
            new_pos = Position(pos.row + dr * step, pos.col + dc * step, pos.board)
            if not new_pos.is_within_board():
                break
            target_moves = new_pos.evaluate_target(self)
            valid_moves.extend(target_moves)
            if target_moves and pos.board[new_pos.row][new_pos.col] != " ":
                break
        return valid_moves

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

