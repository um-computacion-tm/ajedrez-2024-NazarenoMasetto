from juego.board import Board

class Chess:
    def __init__(self):
        self.board = Board()
        self.turn = "WHITE"

    def is_playing(self):
        return True

    def move(self, from_row, from_col, to_row, to_col):
        # Validar coordenadas
        if not (0 <= from_row < 8 and 0 <= from_col < 8 and 0 <= to_row < 8 and to_col < 8):
            raise ValueError("Coordenadas fuera del tablero")

        # Obtener la pieza en la posición de origen
        piece = self.board.get_piece_at((from_row, from_col))
        if piece is None:
            raise ValueError("No hay pieza en la posición de origen")

        # Depuración: imprimir el turno actual y el color de la pieza seleccionada
        print(f"Turno actual: {self.turn}, color de la pieza seleccionada: {piece.get_color()}")

        # Convertir ambos valores a mayúsculas para evitar problemas de sensibilidad a mayúsculas
        if piece.get_color().upper() != self.turn.upper():
            raise ValueError("La pieza no es de tu color")

        # Cambiar valid_positions a valid_moves
        if (to_row, to_col) not in piece.valid_moves((from_row, from_col), self.board.get_board()):
            raise ValueError("Movimiento inválido")

        # Mover la pieza
        self.board.move_piece((from_row, from_col), (to_row, to_col))

        # Cambiar el turno
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
