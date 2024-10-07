from juego.piece import Piece

class Knight(Piece):
    
    KNIGHT_MOVES = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

    def __init__(self, color):
        super().__init__(color)

    def valid_moves(self, current_position, board):
        row, col = current_position
        moves = []

        for move in Knight.KNIGHT_MOVES:
            moves += self._get_knight_move(row, col, board, move)

        return moves

    def _get_knight_move(self, row, col, board, move):
        """Calcula y valida un movimiento del caballo."""
        dr, dc = move
        new_row, new_col = row + dr, col + dc
        moves = []

        if self._is_within_board(new_row, new_col) and self._is_valid_move(new_row, new_col, board):
            moves.append((new_row, new_col))

        return moves

    def _is_within_board(self, row, col):
        """Verifica si una posición está dentro de los límites del tablero."""
        return 0 <= row < 8 and 0 <= col < 8

    def _is_valid_move(self, row, col, board):
        """Verifica si un movimiento es válido."""
        target_piece = board[row][col]
        return target_piece == " " or target_piece.get_color() != self.get_color()

    def get_symbol(self):
        return "N" if self.get_color() == 'White' else "n"


