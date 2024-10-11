from juego.piece import Piece

class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)

    def valid_moves(self, current_position, board):
        row, col = current_position
        # Movimientos en todas las direcciones posibles (horizontales, verticales, diagonales)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        return self._explore_directions(row, col, directions, board)

    def get_symbol(self):
        return "Q" if self.get_color() == 'White' else "q"

    def _explore_directions(self, row, col, directions, board):
        valid_moves = []
        for dr, dc in directions:
            valid_moves.extend(self._explore_direction(row, col, dr, dc, board))
        return valid_moves

    def _explore_direction(self, row, col, dr, dc, board):
        moves = []
        new_row, new_col = row + dr, col + dc
        while self._is_within_board(new_row, new_col):
            if board[new_row][new_col] == " ":
                moves.append((new_row, new_col))
            elif board[new_row][new_col].get_color() != self.get_color():
                moves.append((new_row, new_col))  # Captura válida
                break
            else:
                break
            new_row += dr
            new_col += dc
        return moves
