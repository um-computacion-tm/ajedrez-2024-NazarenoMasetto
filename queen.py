from piece import Piece

class Queen(Piece):
    DIRECTIONS = [  # Direcciones de movimiento, se pueden reutilizar en otras clases
        (-1, 0), (1, 0),   # Vertical
        (0, -1), (0, 1),   # Horizontal
        (-1, -1), (-1, 1), # Diagonales superiores
        (1, -1), (1, 1)    # Diagonales inferiores
    ]

    def __init__(self, color):
        super().__init__(color)

    def valid_moves(self, current_position, board):
        moves = []

        
        for direction in Queen.DIRECTIONS:
            moves.extend(self._collect_moves_in_direction(current_position, direction, board))

        return moves

    def _collect_moves_in_direction(self, current_position, direction, board):
        """Función que recorre en una dirección y agrega movimientos válidos."""
        moves = []
        for new_pos in self._generate_positions_in_direction(current_position, direction):
            if self._is_valid_move(new_pos, board):
                moves.append(new_pos)
            if not self._can_continue(new_pos, board):
                break
        return moves

    def _generate_positions_in_direction(self, current_position, direction):
        """Genera todas las posiciones en una dirección dada a partir de la posición actual."""
        row, col = current_position
        dr, dc = direction
        new_row, new_col = row + dr, col + dc
        while 0 <= new_row < 8 and 0 <= new_col < 8:
            yield (new_row, new_col)
            new_row += dr
            new_col += dc

    def _is_valid_move(self, position, board):
        """Comprueba si la posición es un movimiento válido (casilla vacía o captura)."""
        row, col = position
        return board[row][col] == " " or board[row][col].get_color() != self.get_color()

    def _can_continue(self, position, board):
        """Determina si podemos continuar recorriendo después de una posición."""
        row, col = position
        return board[row][col] == " "

    def get_symbol(self):
        return "Q" if self.get_color() == 'White' else "q"
