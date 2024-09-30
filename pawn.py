from piece import Piece
class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)

    def valid_moves(self, current_position, board):
        row, col = current_position
        moves = []

        direction = self.get_direction()
        
        # Movimiento hacia adelante
        self.add_forward_moves(current_position, direction, board, moves)

        # Capturas diagonales
        self.add_diagonal_captures(current_position, direction, board, moves)

        return moves

    def get_direction(self):
        # Determina la dirección del peón en función de su color
        return -1 if self.get_color() == 'White' else 1

    def add_forward_moves(self, position, direction, board, moves):
        row, col = position
        new_position = (row + direction, col)
        # Movimiento hacia adelante (una casilla)
        if board[new_position[0]][new_position[1]] == " ":
            moves.append(new_position)

            # Movimiento doble hacia adelante (primer movimiento)
            if self.is_first_move(row):
                new_position = (row + 2 * direction, col)
                if board[new_position[0]][new_position[1]] == " ":
                    moves.append(new_position)

    def is_first_move(self, row):
        # Verifica si el peón está en su posición inicial
        return (self.get_color() == 'White' and row == 6) or (self.get_color() == 'Black' and row == 1)

    def add_diagonal_captures(self, position, direction, board, moves):
        row, col = position
        # Captura diagonal izquierda
        if col - 1 >= 0:
            self.check_capture(position, -1, direction, board, moves)

        # Captura diagonal derecha
        if col + 1 <= 7:
            self.check_capture(position, 1, direction, board, moves)

    def check_capture(self, position, col_offset, direction, board, moves):
        row, col = position
        new_position = (row + direction, col + col_offset)
        # Verifica si hay una captura válida en una diagonal
        if board[new_position[0]][new_position[1]] != " ":
            if board[new_position[0]][new_position[1]].get_color() != self.get_color():
                moves.append(new_position)

    def get_symbol(self):
        # Retorna el símbolo del peón en función de su color
        return "P" if self.get_color() == 'White' else "p"