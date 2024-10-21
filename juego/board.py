from juego.piece import Piece

class Board:
    def __init__(self):
        self.grid = [
            ['r', 'N', 'b', 'q', 'k', 'b', 'N', 'r'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', 'K', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        ]
        self.turn = 'White'

    def move_piece(self, start, end):
        start_pos = self.position_to_indices(start)
        end_pos = self.position_to_indices(end)
        piece = self.grid[start_pos[0]][start_pos[1]]
        if piece == " ":
            raise ValueError("No hay ninguna pieza en la posición de inicio")
        self.grid[end_pos[0]][end_pos[1]] = piece
        self.grid[start_pos[0]][start_pos[1]] = " "

    def position_to_indices(self, pos):
        row = int(pos[1]) - 1
        col = ord(pos[0]) - ord('a')
        return row, col

    def get_symbol(self, piece):
        return piece.get_symbol() if isinstance(piece, Piece) else " "
