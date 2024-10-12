from juego.piece import Piece

class King(Piece):
    def __init__(self, color):
        super().__init__(color)

    def valid_moves(self, current_position, board):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        return self._get_valid_moves(current_position, directions, board, max_steps=1)

    def get_symbol(self):
        return "K" if self.get_color() == 'White' else "k"

    def _get_valid_moves(self, current_position, directions, board, max_steps):
        """
        Función auxiliar que reutiliza la lógica para obtener los movimientos válidos,
        explorando cada dirección hasta un máximo de pasos.
        """
        valid_moves = []
        for direction in directions:
            valid_moves.extend(self._explore_direction(current_position, direction, board, max_steps))
        return valid_moves

    def _explore_direction(self, current_position, direction, board, max_steps):
        """
        Explora una dirección desde la posición actual y devuelve movimientos válidos,
        ya sea movimientos a espacios vacíos o capturas.
        """
        valid_moves = []
        row, col = current_position
        dr, dc = direction
        for step in range(1, max_steps + 1):
            new_row, new_col = row + dr * step, col + dc * step
            if not self._is_within_board(new_row, new_col):
                break
            if board[new_row][new_col] == " ":
                valid_moves.append((new_row, new_col))
            elif board[new_row][new_col].get_color() != self.get_color():
                valid_moves.append((new_row, new_col))  # Captura válida
                break
            else:
                break
        return valid_moves

    def _is_within_board(self, row, col):
        """Verifica si una posición está dentro de los límites del tablero."""
        return 0 <= row < 8 and 0 <= col < 8

