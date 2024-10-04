from juego.piece import Piece

class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)

    def valid_moves(self, current_position, board):
        row, col = current_position
        moves = []

        direction = self.get_direction()

        # Movimiento hacia adelante
        self.add_move_if_valid(row + direction, col, board, moves)
        if self.is_first_move(row) and self.is_valid_move(row + 2 * direction, col, board):
            self.add_move_if_valid(row + 2 * direction, col, board, moves)

        # Capturas diagonales
        for col_offset in [-1, 1]:
            self.add_capture_if_valid(row + direction, col + col_offset, board, moves)

        return moves

    def get_direction(self):
        return -1 if self.get_color() == 'White' else 1

    def add_move_if_valid(self, row, col, board, moves):
        if self.is_valid_position(row, col) and board[row][col] == " ":
            moves.append((row, col))

    def add_capture_if_valid(self, row, col, board, moves):
        if self.is_valid_position(row, col) and board[row][col] != " " and board[row][col].get_color() != self.get_color():
            moves.append((row, col))

    def is_valid_position(self, row, col):
        return 0 <= row <= 7 and 0 <= col <= 7

    def is_first_move(self, row):
        return (self.get_color() == 'White' and row == 6) or (self.get_color() == 'Black' and row == 1)

    def get_symbol(self):
        return "P" if self.get_color() == 'White' else "p"
