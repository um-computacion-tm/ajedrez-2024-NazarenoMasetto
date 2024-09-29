from piece import Piece

class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)

    def valid_moves(self, current_position, board):
        """Genera los movimientos válidos del peón."""
        row, col = current_position
        moves = []

        direction = -1 if self.get_color() == 'White' else 1

        # Verifica el movimiento hacia adelante (una casilla)
        self._add_forward_move(row, col, direction, moves, board)

        # Verifica el movimiento doble hacia adelante
        self._add_double_move(row, col, direction, moves, board)

        # Verifica las capturas diagonales
        self._add_diagonal_captures(row, col, direction, moves, board)

        return moves

    def _add_forward_move(self, row, col, direction, moves, board):
        """Agrega el movimiento hacia adelante de un peón si es válido."""
        if self.is_empty_square(row + direction, col, board):
            moves.append((row + direction, col))

    def _add_double_move(self, row, col, direction, moves, board):
        """Agrega el movimiento doble hacia adelante del peón si es válido."""
        if (self.get_color() == 'White' and row == 6) or (self.get_color() == 'Black' and row == 1):
            if self.is_empty_square(row + 2 * direction, col, board):
                moves.append((row + 2 * direction, col))

    def _add_diagonal_captures(self, row, col, direction, moves, board):
        """Agrega las capturas diagonales del peón si son válidas."""
        for dc in [-1, 1]:  # Capturas hacia la izquierda y derecha
            target_row, target_col = row + direction, col + dc
            if self.is_valid_capture(target_row, target_col, board):
                moves.append((target_row, target_col))

    def is_empty_square(self, row, col, board):
        """Verifica si una casilla está vacía."""
        return 0 <= row < 8 and 0 <= col < 8 and board[row][col] == " "

    def is_valid_capture(self, row, col, board):
        """Verifica si una captura es válida."""
        return (0 <= row < 8 and 0 <= col < 8 and 
                board[row][col] != " " and 
                board[row][col].get_color() != self.get_color())

    def get_symbol(self):
        """Devuelve el símbolo correspondiente al peón."""
        return "P" if self.get_color() == 'White' else "p"
