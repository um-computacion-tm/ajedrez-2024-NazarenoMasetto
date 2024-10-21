from juego.piece import Piece

class King(Piece):
    def __init__(self, color):
        super().__init__(color)

    def get_symbol(self):
        return 'K' if self.get_color() == 'White' else 'k'

    def valid_moves(self, current_position, board):
        possible_moves = self._get_king_moves()
        return self.calculate_valid_moves(current_position, possible_moves, board)

    @staticmethod
    def _get_king_moves():
        return [
            {"row": 0, "col": 1}, {"row": 1, "col": 0}, 
            {"row": 0, "col": -1}, {"row": -1, "col": 0},  # Movimientos ortogonales
            {"row": 1, "col": 1}, {"row": 1, "col": -1}, 
            {"row": -1, "col": 1}, {"row": -1, "col": -1}  # Movimientos diagonales
        ]

