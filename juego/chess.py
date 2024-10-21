from juego.board import Board

class Chess:
    def __init__(self):
        self.board = Board()
        self.turn = "WHITE"

    def move(self, from_row, from_col, to_row, to_col):
        piece = self.board.get_piece_at((from_row, from_col))
        if not piece:
            raise ValueError("No hay ninguna pieza en la posición de inicio")

        if piece.get_color().upper() != self.turn:
            raise ValueError("Es el turno de las " + self.turn)

        if not self.board.is_valid_move(piece, (from_row, from_col), (to_row, to_col)):
            raise ValueError("Movimiento no permitido para la pieza seleccionada")

        self.board.move_piece((from_row, from_col), (to_row, to_col))
        self.change_turn()

    def change_turn(self):
        self.turn = "BLACK" if self.turn == "WHITE" else "WHITE"

    def get_board(self):
        return self.board.get_board()
