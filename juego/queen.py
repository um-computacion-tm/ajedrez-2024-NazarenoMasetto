from juego.piece import Piece

class Queen(Piece):
    def __init__(self, color):
        
        super().__init__(color)

    def valid_moves(self, current_position, board):
        
        row, col = current_position
        moves = []

        
        directions = [
            (-1, 0), (1, 0),  # Vertical
            (0, -1), (0, 1),  # Horizontal
            (-1, -1), (-1, 1),  # Diagonal
            (1, -1), (1, 1)    # Diagonal
        ]

       
        moves = self._get_moves_in_directions(row, col, directions, board)

        return moves

    def _get_moves_in_directions(self, row, col, directions, board):
        
        valid_moves = []
        for dr, dc in directions:
            valid_moves.extend(self._explore_direction(row, col, dr, dc, board))
        return valid_moves

    def _explore_direction(self, row, col, dr, dc, board):
        
        moves_in_direction = []
        new_row, new_col = row + dr, col + dc
        while self._is_within_board(new_row, new_col):
            if board[new_row][new_col] == " ":
                moves_in_direction.append((new_row, new_col))
            elif board[new_row][new_col].get_color() != self.get_color():
                moves_in_direction.append((new_row, new_col))  # Captura válida
                break  # Detener después de capturar
            else:
                break  
            new_row += dr
            new_col += dc
        return moves_in_direction

    def _is_within_board(self, row, col):
        
        return 0 <= row < 8 and 0 <= col < 8

    def get_symbol(self):
      
        return "Q" if self.get_color() == 'White' else "q"

    