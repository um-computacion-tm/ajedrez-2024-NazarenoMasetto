from Moveexplorer import MoveExplorer
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
        explorer = MoveExplorer(self, board)
        return explorer.explore(row, col, moves, limit)

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
