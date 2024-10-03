from piece import Piece
class Queen(Piece):
    def __init__(self, color):
  
        super().__init__(color)

    def valid_moves(self, current_position, board):
        
        row, col = current_position
        moves = []
        
        # Definir las 8 direcciones de movimiento (vertical, horizontal y diagonal)
        directions = [
            (-1, 0), (1, 0),  # Movimientos verticales (arriba y abajo)
            (0, -1), (0, 1),  # Movimientos horizontales (izquierda y derecha)
            (-1, -1), (-1, 1),  # Movimientos diagonales (arriba-izquierda, arriba-derecha)
            (1, -1), (1, 1)    # Movimientos diagonales (abajo-izquierda, abajo-derecha)
        ]

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            # Continuar en una dirección hasta que encontremos un borde del tablero o una pieza
            while 0 <= new_row < 8 and 0 <= new_col < 8:
                if board[new_row][new_col] == " ":
                    moves.append((new_row, new_col))  # Casilla vacía, movimiento válido
                elif board[new_row][new_col].get_color() != self.get_color():
                    moves.append((new_row, new_col))  # Captura válida
                    break  # Detener después de capturar
                else:
                    break  # No puede moverse más allá de una pieza del mismo color
                new_row += dr
                new_col += dc

        return moves

    def get_symbol(self):
      
        return "Q" if self.get_color() == 'White' else "q"
