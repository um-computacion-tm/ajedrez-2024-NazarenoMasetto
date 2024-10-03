from piece import Piece

class Queen(Piece):
    DIRECTIONS = [  
        (-1, 0), (1, 0),   # Vertical
        (0, -1), (0, 1),   # Horizontal
        (-1, -1), (-1, 1), # Diagonales superiores
        (1, -1), (1, 1)    # Diagonales inferiores
    ]

    def __init__(self, color):
        super().__init__(color)

    def valid_moves(self, current_position, board):
        """Calcula los movimientos válidos de la reina."""
        return self._generate_linear_moves(current_position, board, Queen.DIRECTIONS)

    def _generate_linear_moves(self, current_position, board, directions):
        """Genera los movimientos lineales (reina, torre, alfil)."""
        moves = []

        for direction in directions:
            moves.extend(self._collect_moves_in_direction(current_position, direction, board))

        return moves

    def _collect_moves_in_direction(self, current_position, direction, board):
        """Función auxiliar que explora una dirección dada y recoge movimientos válidos."""
        moves = []
        for new_pos in self._generate_positions_in_direction(current_position, direction):
            if self._is_valid_move(new_pos, board):
                moves.append(new_pos)
            if not self._can_continue(new_pos, board):
                break
        return moves

    def _generate_positions_in_direction(self, current_position, direction):
        """Genera todas las posiciones en una dirección dada desde la posición actual."""
        row, col = current_position
        dr, dc = direction
        new_row, new_col = row + dr, col + dc
        while self._is_within_board(new_row, new_col):
            yield (new_row, new_col)
            new_row += dr
            new_col += dc

    def _is_within_board(self, row, col):
        """Verifica si la posición está dentro del tablero."""
        return 0 <= row < 8 and 0 <= col < 8

    def _is_valid_move(self, position, board):
        """Comprueba si la posición es un movimiento válido (casilla vacía o captura)."""
        row, col = position
        return board[row][col] == " " or board[row][col].get_color() != self.get_color()

    def _can_continue(self, position, board):
        """Determina si se puede continuar después de una posición."""
        row, col = position
        return board[row][col] == " "

    def get_symbol(self):
        """Devuelve el símbolo que representa la reina en el tablero."""
        return "Q" if self.get_color() == 'White' else "q"
