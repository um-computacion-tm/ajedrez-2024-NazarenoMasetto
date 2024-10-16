from juego.piece import Piece

class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)

    def valid_moves(self, current_position, board):
        knight_moves = self._get_knight_moves()  # Usamos una función para obtener los movimientos de un caballo
        row, col = current_position
        return self._get_valid_moves(row, col, knight_moves, board)

    def get_symbol(self):
        return "N" if self.get_color() == 'White' else "n"

    def _get_knight_moves(self):
        return [
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)
        ]
