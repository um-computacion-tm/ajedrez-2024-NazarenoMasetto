from juego.piece import Piece
class King(Piece):
    def __init__(self, color):
        super().__init__(color)

    def get_symbol(self):
        return 'K'

    def valid_moves(self, current_position, board):
        possible_moves = self._get_moves([(0, 1), (1, 0), (0, -1), (-1, 0),
                                           (1, 1), (1, -1), (-1, 1), (-1, -1)])
        return self.calculate_valid_moves(current_position, possible_moves, board)

    @staticmethod
    def _get_moves(directions):
        return directions
