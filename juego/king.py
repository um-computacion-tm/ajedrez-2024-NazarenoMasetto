from juego.piece import Piece

class King(Piece):
    def __init__(self, color):
        super().__init__(color)

    def valid_moves(self, current_position, board):
        row, col = current_position
        king_moves = [
            (-1, 0), (1, 0),  # Vertical
            (0, -1), (0, 1),  # Horizontal
            (-1, -1), (-1, 1), (1, -1), (1, 1)  # Diagonal
        ]
        valid_moves = []

        for move in king_moves:
            new_row, new_col = row + move[0], col + move[1]
            # Verifica si la nueva posición es válida
            if self._is_valid_move(new_row, new_col, board):
                valid_moves.append((new_row, new_col))

        return valid_moves

    def get_symbol(self):
        return "K" if self.get_color() == 'White' else "k"

    def _is_within_board(self, row, col, board):
        """Comprueba si una posición está dentro del tablero."""
        return 0 <= row < len(board) and 0 <= col < len(board[0])
    
    def _is_valid_move(self, row, col, board):
        """Verifica si el movimiento es válido."""
        if not self._is_within_board(row, col, board):
            return False
        target_square = board[row][col]
        # Devuelve True si la casilla está vacía o contiene una pieza del color opuesto
        return target_square == " " or target_square.get_color() != self.get_color()
