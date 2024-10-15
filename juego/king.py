from juego.piece import Piece

class King(Piece):
    def __init__(self, color):
        super().__init__(color)

    def valid_moves(self, current_position, board):
        directions = self._get_directions()  # Usamos la misma función que en Queen
        row, col = current_position
        valid_moves = []

        for dr, dc in directions:
            self._add_valid_move(row + dr, col + dc, board, valid_moves)

        return valid_moves

    def _get_directions(self):
        return [
            (-1, 0), (1, 0), (0, -1), (0, 1),  # Vertical y Horizontal
            (-1, -1), (-1, 1), (1, -1), (1, 1)  # Diagonales
        ]

    def _add_valid_move(self, new_row, new_col, board, valid_moves):
        if self._is_within_board(new_row, new_col):
            target_square = board[new_row][new_col]
            if target_square == " " or target_square.get_color() != self.get_color():
                valid_moves.append((new_row, new_col))

    def _is_within_board(self, row, col):
        return 0 <= row < 8 and 0 <= col < 8

    def get_symbol(self):
        return "K" if self.get_color() == 'White' else "k"
