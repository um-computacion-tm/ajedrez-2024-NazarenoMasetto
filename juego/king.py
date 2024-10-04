from juego.piece import Piece


def get_standard_directions():
    """
    Devuelve las direcciones estándar para piezas que se mueven en línea recta y diagonal.
    """
    return [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

class King(Piece):
    def __init__(self, color):
        super().__init__(color)

    def valid_moves(self, current_position, board):
        """
        Calcula los movimientos válidos del rey según las reglas del ajedrez.
        """
        directions = get_standard_directions()  # Usamos la función compartida para obtener las direcciones
        return self._generate_king_moves(current_position, board, directions)

    def _generate_king_moves(self, current_position, board, directions):
        """
        Función auxiliar para generar movimientos válidos del rey en las direcciones especificadas.
        """
        moves = []
        for direction in directions:
            new_position = self._get_new_position(current_position, direction)
            if self._is_within_bounds(new_position) and self._is_valid_move(new_position, board):
                moves.append(new_position)
        return moves

    def _get_new_position(self, current_position, direction):
        """
        Calcula la nueva posición a partir de la posición actual y una dirección.
        """
        row, col = current_position
        dr, dc = direction
        return row + dr, col + dc

    def _is_within_bounds(self, position):
        """
        Verifica si una posición está dentro de los límites del tablero.
        """
        row, col = position
        return 0 <= row < 8 and 0 <= col < 8

    def _is_valid_move(self, position, board):
        """
        Verifica si una casilla está vacía o contiene una pieza del oponente.
        """
        row, col = position
        piece = board[row][col]
        return piece == " " or piece.get_color() != self.get_color()

    def get_symbol(self):
        """
        Devuelve el símbolo que representa al rey en el tablero.
        """
        return "K" if self.get_color() == 'White' else "k"
