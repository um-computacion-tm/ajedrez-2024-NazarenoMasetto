from juego.piece import Piece

class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)

    def valid_moves(self, current_position, board):
        row, col = current_position
        directions = self.get_directions()
        valid_moves = []
        for direction in directions:
            valid_moves.extend(self._explore_direction(row, col, direction, board))
        return valid_moves

    def get_symbol(self):
        return "Q" if self.get_color() == 'White' else "q"