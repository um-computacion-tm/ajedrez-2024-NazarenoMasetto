from piece import Piece
class Pawn(Piece):
    def __init__(self, color):
        
        super().__init__(color)

    def valid_moves(self, current_position, board):
        
        row, col = current_position
        moves = []
        
        # Dirección de movimiento: hacia arriba para las blancas, hacia abajo para las negras
        direction = -1 if self.get_color() == 'White' else 1

        # Movimiento hacia adelante (una casilla)
        if board[row + direction][col] == " ":
            moves.append((row + direction, col))

            # Movimiento doble hacia adelante (solo en el primer movimiento)
            if (self.get_color() == 'White' and row == 6) or (self.get_color() == 'Black' and row == 1):
                if board[row + 2 * direction][col] == " ":
                    moves.append((row + 2 * direction, col))

        # Captura diagonal izquierda
        if col - 1 >= 0 and board[row + direction][col - 1] != " ":
            if board[row + direction][col - 1].get_color() != self.get_color():
                moves.append((row + direction, col - 1))

        # Captura diagonal derecha
        if col + 1 <= 7 and board[row + direction][col + 1] != " ":
            if board[row + direction][col + 1].get_color() != self.get_color():
                moves.append((row + direction, col + 1))

        return moves

    def get_symbol(self):
        
        return "P" if self.get_color() == 'White' else "p"
