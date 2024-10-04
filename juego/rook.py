from juego.piece import Piece

class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)

    def valid_moves(self, current_position, board):
        """
        Calcula los movimientos válidos de la torre según las reglas del ajedrez.
        """
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Movimientos verticales y horizontales
        return self._generate_linear_moves(current_position, board, directions)

    def _generate_linear_moves(self, current_position, board, directions):
        """
        Función auxiliar para generar movimientos lineales (como los de torre y alfil).
        """
        moves = []

        for direction in directions:
            moves.extend(self._explore_direction(current_position, direction, board))

        return moves

    def _explore_direction(self, current_position, direction, board):
        """
        Explora una dirección específica hasta que se encuentre un borde del tablero o una pieza.
        """
        row, col = current_position
        dr, dc = direction
        moves = []

        new_row, new_col = row + dr, col + dc
        
        while self.is_within_bounds(new_row, new_col):  
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
        """Devuelve el símbolo que representa la torre en el tablero."""
        return "R" if self.get_color() == 'White' else "r"
