from piece import Piece

class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)

    def valid_moves(self, current_position, board):
        """Calcula los movimientos válidos de la reina, combinando movimientos lineales y diagonales."""
        directions = [
            (-1, 0), (1, 0),   # Vertical
            (0, -1), (0, 1),   # Horizontal
            (-1, -1), (-1, 1), # Diagonales superiores
            (1, -1), (1, 1)    # Diagonales inferiores
        ]
        return self._generate_moves(current_position, board, directions)

    def _generate_moves(self, current_position, board, directions):
        """Genera movimientos válidos en múltiples direcciones."""
        moves = []
        row, col = current_position
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            
            while self._is_within_board(new_row, new_col):
                piece = board[new_row][new_col]
                if piece == " ":
                    moves.append((new_row, new_col))  # Casilla vacía
                elif piece.get_color() != self.get_color():
                    moves.append((new_row, new_col))  # Captura
                    break  # No puede moverse más allá de una pieza enemiga
                else:
                    break  # Pieza aliada bloquea el camino

                new_row += dr
                new_col += dc

        return moves

    def _is_within_board(self, row, col):
        """Verifica si la posición está dentro de los límites del tablero."""
        return 0 <= row < 8 and 0 <= col < 8

    def get_symbol(self):
        """Devuelve el símbolo que representa la reina en el tablero."""
        return "Q" if self.get_color() == 'White' else "q"
