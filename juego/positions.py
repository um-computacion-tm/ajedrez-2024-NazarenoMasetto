class Position:
    def __init__(self, row, col, board):
        self.row = row
        self.col = col
        self.board = board

    def is_within_board(self):
        return 0 <= self.row < 8 and 0 <= self.col < 8

    def evaluate_target(self, piece):
        """Evalúa si la casilla está vacía, contiene una pieza oponente o está ocupada por una pieza aliada."""
        target_square = self.board[self.row][self.col]
        if target_square == " ":
            return [(self.row, self.col)]  # Movimiento vacío
        elif target_square.get_color() != piece.get_color():
            return [(self.row, self.col)]  # Captura
        return []  # Ocupada por una pieza aliada
