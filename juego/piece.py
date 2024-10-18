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

    @staticmethod
    def _calculate_new_position(current_position, move):
        """
        Calcula una nueva posición sumando los valores del movimiento a la posición actual.
        :param current_position: Tupla (fila, columna).
        :param move: Tupla (delta_fila, delta_columna) que representa el movimiento.
        :return: Nueva posición (fila, columna).
        """
        return current_position[0] + move[0], current_position[1] + move[1]

    @staticmethod
    def _is_within_board(row, col):
        return 0 <= row < 8 and 0 <= col < 8


