from juego.piece import Piece

class King(Piece):
    def __init__(self, color):
        super().__init__(color)

    def valid_moves(self, current_position, board):
        row, col = current_position
        directions = self._get_king_directions()
        return self._get_valid_moves(row, col, directions, board)

    def get_symbol(self):
        return "K" if self.get_color() == 'White' else "k"

    def _get_king_directions(self):
        return [
            (-1, 0), (1, 0), (0, -1), (0, 1),  # Vertical y horizontal
            (-1, -1), (-1, 1), (1, -1), (1, 1)  # Diagonales
        ]

