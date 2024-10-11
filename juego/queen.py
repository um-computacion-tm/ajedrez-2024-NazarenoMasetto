from juego.piece import Piece

class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)

    def valid_moves(self, current_position, board):
        row, col = current_position
        directions = [
            (-1, 0), (1, 0),  # Vertical
            (0, -1), (0, 1),  # Horizontal
            (-1, -1), (-1, 1),  # Diagonales
            (1, -1), (1, 1)
        ]
        return self._get_valid_moves(row, col, directions, board, max_steps=8)

    def get_symbol(self):
        return "Q" if self.get_color() == 'White' else "q"
    
    def _get_valid_moves(self, row, col, directions, board, max_steps):
        valid_moves = []
        for dr, dc in directions:
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
        return 0 <= row < 8 and 0 <= col < 8

