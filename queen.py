from piece import Piece

class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)

    def valid_moves(self, current_position, board):
        row, col = current_position
        moves = []

        # Definimos las direcciones de movimiento de la reina
        directions = [
            (-1, 0), (1, 0),   # Vertical
            (0, -1), (0, 1),   # Horizontal
            (-1, -1), (-1, 1), # Diagonales superiores
            (1, -1), (1, 1)    # Diagonales inferiores
        ]

        # Recorremos todas las direcciones y añadimos los movimientos válidos
        for direction in directions:
            moves.extend(self._traverse_direction(current_position, direction, board))

        return moves

    def _traverse_direction(self, current_position, direction, board):
        moves = []
        row, col = current_position
        dr, dc = direction
        new_row, new_col = row + dr, col + dc

        # Recorremos el tablero en la dirección dada
        while 0 <= new_row < 8 and 0 <= new_col < 8:
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

    def get_symbol(self):
        return "Q" if self.get_color() == 'White' else "q"
