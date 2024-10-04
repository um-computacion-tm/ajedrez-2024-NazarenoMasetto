from juego.piece import Piece

class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)

    def valid_moves(self, current_position, board):
        row, col = current_position
        moves = []
        
        # Definir las 8 direcciones de movimiento
        directions = [
            (-1, 0), (1, 0),  # Movimientos verticales
            (0, -1), (0, 1),  # Movimientos horizontales
            (-1, -1), (-1, 1),  # Movimientos diagonales hacia arriba
            (1, -1), (1, 1)  # Movimientos diagonales hacia abajo
        ]

        # Recorremos cada dirección y añadimos movimientos válidos
        for direction in directions:
            moves += self._get_moves_in_direction(current_position, board, direction)

        return moves

    def _get_moves_in_direction(self, current_position, board, direction):
        """Genera movimientos válidos en una dirección dada."""
        row, col = current_position
        dr, dc = direction
        moves = []
        
        new_row, new_col = row + dr, col + dc
        while 0 <= new_row < 8 and 0 <= new_col < 8:
            if board[new_row][new_col] == " ":
                moves.append((new_row, new_col))  # Casilla vacía
            elif board[new_row][new_col].get_color() != self.get_color():
                moves.append((new_row, new_col))  # Captura válida
                break  # Detener después de capturar
            else:
                break  # Pieza del mismo color, detener
            new_row += dr
            new_col += dc

        return moves

    def get_symbol(self):
        return "Q" if self.get_color() == 'White' else "q"
