from juego.piece import Piece

class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)

    def valid_moves(self, current_position, board):
        row, col = current_position
        knight_moves = self._get_knight_moves()  # Obtiene los movimientos del caballo
        return self._get_valid_moves(row, col, knight_moves, board)

    def get_symbol(self):
        return "N" if self.get_color() == 'White' else "n"

    def _get_knight_moves(self):
        # Movimientos en forma de L del caballo
        return [
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)
        ]
