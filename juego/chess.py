from juego.board import Board

class Chess:
    def __init__(self):
        self.board = Board()
        self.turn = "WHITE"

    def is_playing(self):
        return True

    def move(self, from_row, from_col, to_row, to_col):
        # validate coords
        if not (0 <= from_row < 8 and 0 <= from_col < 8 and 0 <= to_row < 8 and 0 <= to_col < 8):
            raise ValueError("Coordenadas fuera del tablero")

        piece = self.board.get_piece(from_row, from_col)
        if piece is None:
            raise ValueError("No hay pieza en la posición de origen")

        if piece.color != self.turn:
            raise ValueError("La pieza no es de tu color")

        if not piece.valid_positions(from_row, from_col, to_row, to_col):
            raise ValueError("Movimiento inválido")

        
        self.board.move_piece(from_row, from_col, to_row, to_col)

  
        self.change_turn()

  
    def turn(self):
        return self.turn

    def show_board(self):
        return str(self.board)

    def change_turn(self):
        if self.turn == "WHITE":
            self.turn = "BLACK"
        else:
            self.turn = "WHITE"