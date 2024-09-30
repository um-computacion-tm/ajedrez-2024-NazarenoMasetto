from piece import Piece

class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)

    def valid_moves(self, current_position, board):
        row, col = current_position
        moves = []

        direction = self.get_direction()
        
        # Movimiento hacia adelante
        self.add_forward_moves(row, col, direction, board, moves)

        # Capturas diagonales
        self.add_diagonal_captures(row, col, direction, board, moves)

        return moves

    def get_direction(self):
        # Determina la dirección del peón en función de su color
        return -1 if self.get_color() == 'White' else 1

    def add_forward_moves(self, row, col, direction, board, moves):
        # Movimiento hacia adelante (una casilla)
        if board[row + direction][col] == " ":
            moves.append((row + direction, col))

            # Movimiento doble hacia adelante (primer movimiento)
            if self.is_first_move(row):
                if board[row + 2 * direction][col] == " ":
                    moves.append((row + 2 * direction, col))

    def is_first_move(self, row):
        # Verifica si el peón está en su posición inicial
        return (self.get_color() == 'White' and row == 6) or (self.get_color() == 'Black' and row == 1)

    def add_diagonal_captures(self, row, col, direction, board, moves):
        # Captura diagonal izquierda
        if col - 1 >= 0:
            self.check_capture(row, col - 1, direction, board, moves)

        # Captura diagonal derecha
        if col + 1 <= 7:
            self.check_capture(row, col + 1, direction, board, moves)

    def check_capture(self, row, col, direction, board, moves):
        # Verifica si hay una captura válida en una diagonal
        if board[row + direction][col] != " ":
            if board[row + direction][col].get_color() != self.get_color():
                moves.append((row + direction, col))

    def get_symbol(self):
        # Retorna el símbolo del peón en función de su color
        return "P" if self.get_color() == 'White' else "p"
