from juego.piece import Piece

def is_within_board(row, col):
    """Verifica si una posición está dentro de los límites del tablero."""
    return 0 <= row < 8 and 0 <= col < 8

def get_standard_directions():
    """
    Devuelve las direcciones estándar para piezas que se mueven en línea recta y diagonal.
    """
    return [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

class King(Piece):
    def __init__(self, color):
        super().__init__(color)

    def valid_moves(self, current_position, board):
        directions = get_standard_directions()
        return self._generate_king_moves(current_position, board, directions)

    def _generate_king_moves(self, current_position, board, directions):
        moves = []
        for direction in directions:
            new_position = self._get_new_position(current_position, direction)
            if is_within_board(*new_position) and self._is_valid_move(new_position, board):
                moves.append(new_position)
        return moves

    def _get_new_position(self, current_position, direction):
        row, col = current_position
        dr, dc = direction
        return row + dr, col + dc

    def _is_valid_move(self, position, board):
        row, col = position
        piece = board[row][col]
        return piece == " " or piece.get_color() != self.get_color()

    def get_symbol(self):
        return "K" if self.get_color() == 'White' else "k"

