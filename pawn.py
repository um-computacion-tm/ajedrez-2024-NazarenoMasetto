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
        if self.is_valid_move(row + direction, col, board):
            moves.append((row + direction, col))
            if self.is_first_move(row):
                if self.is_valid_move(row + 2 * direction, col, board):
                    moves.append((row + 2 * direction, col))

    def is_first_move(self, row):
        # Verifica si el peón está en su posición inicial
        return (self.get_color() == 'White' and row == 6) or (self.get_color() == 'Black' and row == 1)

    def is_valid_move(self, row, col, board):
        return board[row][col] == " "

    def add_diagonal_captures(self, position, direction, board, moves):
        row, col = position
        for col_offset in [-1, 1]:
            if 0 <= col + col_offset <= 7:
                if self.is_valid_capture(row + direction, col + col_offset, board):
                    moves.append((row + direction, col + col_offset))

    def is_valid_capture(self, row, col, board):
        return board[row][col] != " " and board[row][col].get_color() != self.get_color()

    def get_symbol(self):
        # Retorna el símbolo del peón en función de su color
        return "P" if self.get_color() == 'White' else "p"