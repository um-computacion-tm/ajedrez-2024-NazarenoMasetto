from juego.piece import Piece

class King(Piece):
    def __init__(self, color):
        super().__init__(color)

    def valid_moves(self, current_position, board):
       
        row, col = current_position
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        valid_moves = []

        for dr, dc in directions:
            self._add_valid_move(row + dr, col + dc, board, valid_moves)

        return valid_moves

    def _add_valid_move(self, new_row, new_col, board, valid_moves):
        
        if 0 <= new_row < 8 and 0 <= new_col < 8:  # Verificar si está dentro del tablero
            target_square = board[new_row][new_col]
            if target_square == " " or target_square.get_color() != self.get_color():
                valid_moves.append((new_row, new_col))

    def get_symbol(self):
        
        return "K" if self.get_color() == 'White' else "k"
