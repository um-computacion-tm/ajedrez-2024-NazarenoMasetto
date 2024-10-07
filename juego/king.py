from juego.piece import Piece

class King(Piece):
    def __init__(self, color):
        super().__init__(color)

    def valid_moves(self, current_position, board):
        directions = self._get_standard_directions()
        return self._generate_king_moves(current_position, board, directions)

    def _generate_king_moves(self, current_position, board, directions):
        """Genera los movimientos válidos para el rey."""
        moves = []
        for direction in directions:
            new_position = self._get_new_position(current_position, direction)
            if self._is_within_board(*new_position) and self._is_valid_move(new_position, board):
                moves.append(new_position)
        return moves

    def _get_new_position(self, current_position, direction):
        """Calcula la nueva posición basada en la dirección del movimiento."""
        row, col = current_position
        dr, dc = direction
        return row + dr, col + dc

    def _is_within_board(self, row, col):
        """Verifica si una posición está dentro de los límites del tablero."""
        return 0 <= row < 8 and 0 <= col < 8

    def _is_valid_move(self, position, board):
        """Verifica si un movimiento es válido."""
        row, col = position
        piece = board[row][col]
        return piece == " " or piece.get_color() != self.get_color()

    def _get_standard_directions(self):
        """Devuelve las direcciones estándar para el rey."""
        return [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    def get_symbol(self):
        return "K" if self.get_color() == 'White' else "k"


