from piece import Piece
class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)

    def valid_moves(self, current_position, board):
        """
        Calcula los movimientos válidos de la torre según las reglas del ajedrez.
        """
        return self._generate_linear_moves(current_position, board, directions=[
            (-1, 0), (1, 0),  
            (0, -1), (0, 1)   
        ])

    def _generate_linear_moves(self, current_position, board, directions):
        """
        Función auxiliar para generar movimientos lineales (como los de torre y alfil).
        """
        row, col = current_position
        moves = []

        for dr, dc in directions:
            moves.extend(self._explore_direction(row, col, dr, dc, board))
        
        return moves

    def _explore_direction(self, row, col, dr, dc, board):
        """
        Explora una dirección específica hasta que se encuentre un borde del tablero o una pieza.
        """
        moves = []
        new_row, new_col = row + dr, col + dc
        
        while 0 <= new_row < 8 and 0 <= new_col < 8:
            piece = board[new_row][new_col]
            if piece == " ":
                moves.append((new_row, new_col))  
            elif piece.get_color() != self.get_color():
                moves.append((new_row, new_col))  
                break  
            else:
                break  
            new_row += dr
            new_col += dc
        
        return moves

    def get_symbol(self):
        return "R" if self.get_color() == 'White' else "r"
