from juego.piece import Piece

class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)

    def valid_moves(self, current_position, board):
        row, col = current_position
        moves = []
        
        # Reutilizamos las direcciones estándar dentro de la misma clase
        directions = self._get_standard_directions()

        for direction in directions:
            moves += self._get_moves_in_direction(row, col, board, direction)

        return moves

    def _get_standard_directions(self):
        """Devuelve las direcciones estándar para movimientos rectos y diagonales."""
        return [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    def _get_moves_in_direction(self, row, col, board, direction):
        """Genera movimientos válidos en una dirección dada."""
        dr, dc = direction
        moves = []
        new_row, new_col = row + dr, col + dc

        while self._is_within_board(new_row, new_col):
            if board[new_row][new_col] == " ":
                moves.append((new_row, new_col))
            elif board[new_row][new_col].get_color() != self.get_color():
                moves.append((new_row, new_col))
                break
            else:
                break
            new_row += dr
            new_col += dc

        return moves

    def _is_within_board(self, row, col):
        """Verifica si una posición está dentro de los límites del tablero."""
        return 0 <= row < 8 and 0 <= col < 8

    def get_symbol(self):
        return "Q" if self.get_color() == 'White' else "q"


