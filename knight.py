from piece import Piece
class Knight(Piece):
    def __init__(self, color):
        
        super().__init__(color)

    def valid_moves(self, current_position, board):
       
        row, col = current_position
        moves = []
        
        
        knight_moves = [
            (2, 1), (2, -1),  
            (-2, 1), (-2, -1),  
            (1, 2), (1, -2),  
            (-1, 2), (-1, -2)  
        ]

        for dr, dc in knight_moves:
            new_row, new_col = row + dr, col + dc
            
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                if board[new_row][new_col] == " " or board[new_row][new_col].get_color() != self.get_color():
                    moves.append((new_row, new_col))  # Casilla vacía o captura válida

        return moves

    def get_symbol(self):
       
        return "N" if self.get_color() == 'White' else "n"
