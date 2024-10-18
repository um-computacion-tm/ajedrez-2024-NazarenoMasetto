from juego.piece import Piece
from juego.movementpatterns import MovementPatterns

class King(Piece):
    def __init__(self, color):
        super().__init__(color)

    def valid_moves(self, current_position, board):
        row, col = current_position
        king_moves = MovementPatterns.king_moves()  # Usando la clase refactorizada
        return self._get_valid_moves(row, col, king_moves, board)

    def get_symbol(self):
        return "K" if self.get_color() == 'White' else "k"
