from juego.piece import Piece

class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)

    def valid_moves(self, current_position, board):
        row, col = current_position
        knight_moves = self.get_knight_moves()
        return self._get_valid_moves(row, col, knight_moves, board)

    def get_symbol(self):
        return "N" if self.get_color() == 'White' else "n"
