class Piece:
    def __init__(self, color):
        self.__color__ = color

    def get_color(self):
        return self.__color__

    def valid_moves(self, current_position, board):
        raise NotImplementedError

    def get_symbol(self):
        raise NotImplementedError

    def __str__(self):
        return self.get_symbol()

    def _is_within_board(self, row, col):
        """
        Verifica si una posición está dentro de los límites del tablero.
        Este método es compartido por todas las piezas.
        """
        return 0 <= row < 8 and 0 <= col < 8

    def _get_standard_directions(self):
        """
        Devuelve las direcciones estándar para piezas que se mueven en línea recta y diagonal.
        Este método es compartido por piezas como la reina y el rey.
        """
        return [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

