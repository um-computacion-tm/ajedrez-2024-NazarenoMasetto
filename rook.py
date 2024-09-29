from piece import Piece

class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)

    def valid_moves(self, current_position, board):
        """
        Calcula los movimientos válidos de la torre según las reglas del ajedrez.
        """
        return self._generate_linear_moves(current_position, board, directions=[
            (-1, 0), (1, 0),  # Movimientos verticales (arriba y abajo)
            (0, -1), (0, 1)   # Movimientos horizontales (izquierda y derecha)
        ])

    def _generate_linear_moves(self, current_position, board, directions):
        """
        Función auxiliar para generar movimientos lineales (como los de torre y alfil).
        """
        row, col = current_position
        moves = []

        for direction in directions:
            moves.extend(self._explore_direction(current_position, direction, board))
        
        return moves

    def _explore_direction(self, current_position, direction, board):
        """
        Explora una dirección específica hasta que se encuentre un borde del tablero o una pieza.
        """
        moves = []
        row, col = current_position
        dr, dc = direction
        
        new_row, new_col = row + dr, col + dc
        
        while self._is_within_bounds(new_row, new_col):
            piece = board[new_row][new_col]
            if piece == " ":
                moves.append((new_row, new_col))  # Casilla vacía, movimiento válido
            elif piece.get_color() != self.get_color():
                moves.append((new_row, new_col))  # Captura válida
                break  # Detener después de capturar
            else:
                break  # No puede moverse más allá de una pieza del mismo color
            new_row += dr
            new_col += dc
        
        return moves

    def _is_within_bounds(self, row, col):
        """
        Verifica si una posición está dentro de los límites del tablero.
        """
        return 0 <= row < 8 and 0 <= col < 8

    def get_symbol(self):
        return "R" if self.get_color() == 'White' else "r"
