from juego.piece import Piece

class King(Piece):
    def __init__(self, color):
        super().__init__(color)

    def valid_moves(self, current_position, board):
        row, col = current_position
        directions = self._get_king_directions()  # Obtenemos las direcciones del rey
        return self._get_valid_king_moves(row, col, directions, board)

    def get_symbol(self):
        return "K" if self.get_color() == 'White' else "k"

    def _get_king_directions(self):
        return [
            (-1, 0), (1, 0), (0, -1), (0, 1),  # Vertical y horizontal
            (-1, -1), (-1, 1), (1, -1), (1, 1)  # Diagonales
        ]

    def _get_valid_king_moves(self, row, col, directions, board):
        valid_moves = []
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            # Usamos _is_within_board heredado de Piece
            if self._is_within_board(new_row, new_col) and (board[new_row][new_col] == " " or board[new_row][new_col].get_color() != self.get_color()):
                valid_moves.append((new_row, new_col))
        return valid_moves

