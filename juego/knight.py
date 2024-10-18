from juego.piece import Piece
class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)

    def get_symbol(self):
        return 'N'

    def valid_moves(self, current_position, board):
        possible_moves = self._get_knight_moves()
        return self.calculate_valid_moves(current_position, possible_moves, board)

    @staticmethod
    def _get_knight_moves():
        return [
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)
        ]
