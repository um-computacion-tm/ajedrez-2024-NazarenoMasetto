from juego.piece import Piece

class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)

    def valid_moves(self, current_position, board):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Movimientos verticales y horizontales
        return self._generate_linear_moves(current_position, board, directions)

    def _generate_linear_moves(self, current_position, board, directions):
        moves = []
        for direction in directions:
            moves.extend(self._explore_direction(current_position[0], current_position[1], direction, board))
        return moves

    def get_symbol(self):
        return "R" if self.get_color() == 'White' else "r"
