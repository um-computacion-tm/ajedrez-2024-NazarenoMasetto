from piece import Piece
class Knight(Piece):
    # Movimientos estándar para el caballo
    KNIGHT_MOVES = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

    def __init__(self, color):
        super().__init__(color)

    def valid_moves(self, current_position, board):
        row, col = current_position
        moves = []

        # Iterar sobre los movimientos posibles del caballo
        for dr, dc in Knight.KNIGHT_MOVES:
            new_row, new_col = self._calculate_new_position(row, col, dr, dc)
            # Verificar si la nueva posición está dentro del tablero y si es un movimiento válido
            if self._is_within_board(new_row, new_col) and self._is_valid_move(new_row, new_col, board):
                moves.append((new_row, new_col))

        return moves

    def _calculate_new_position(self, row, col, dr, dc):
        """Calcula la nueva posición basada en el movimiento del caballo."""
        return row + dr, col + dc

    def _is_within_board(self, row, col):
        """Verifica si una posición está dentro de los límites del tablero."""
        return 0 <= row < 8 and 0 <= col < 8

    def _is_valid_move(self, row, col, board):
        """Verifica si el movimiento es válido: casilla vacía o captura."""
        target_piece = board[row][col]
        return target_piece == " " or target_piece.get_color() != self.get_color()

    def get_symbol(self):
        """Devuelve el símbolo que representa el caballo en el tablero."""
        return "N" if self.get_color() == 'White' else "n"
