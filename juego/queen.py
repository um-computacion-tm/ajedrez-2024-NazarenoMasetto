from juego.piece import Piece

class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)

    def valid_moves(self, current_position, board):
        directions = self._get_directions()  # Use the base method
        row, col = current_position
        return self._get_valid_moves(row, col, directions, board)

    def get_symbol(self):
        return "Q" if self.get_color() == 'White' else "q"

    def _get_directions(self):
        return [
            (-1, 0), (1, 0),  # Vertical
            (0, -1), (0, 1),  # Horizontal
            (-1, -1), (-1, 1), (1, -1), (1, 1)  # Diagonales
        ]
