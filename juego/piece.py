class Piece:
    def __init__(self, color):
        """
        Constructor de la clase base Piece. 
        :param color: El color de la pieza ('White' o 'Black').
        """
        self.__color__ = color

    def get_color(self):
        """
        Devuelve el color de la pieza.
        :return: 'White' o 'Black', dependiendo del color de la pieza.
        """
        return self.__color__

    def valid_moves(self, current_position, board):
        """
        Método abstracto que deben implementar todas las piezas.
        Define los movimientos válidos para cada tipo de pieza.
        :param current_position: La posición actual de la pieza en coordenadas de matriz.
        :param board: El estado actual del tablero como una lista de listas.
        :return: Una lista de posiciones válidas (en coordenadas de matriz) a las que la pieza puede moverse.
        """
        raise NotImplementedError

    def get_symbol(self):
        """
        Método abstracto para obtener el símbolo que representa a la pieza en el tablero.
        :return: Un string que representa el símbolo de la pieza.
        """
        raise NotImplementedError  # Corrige esta línea, faltaba el 'raise'

    def __str__(self):
        """
        Devuelve la representación de la pieza como una cadena de texto.
        Esto se usa para mostrar la pieza en el tablero.
        :return: El símbolo que representa a la pieza (definido por las subclases).
        """
        return self.get_symbol()

    def _is_within_board(self, row, col):
        """
        Verifica si una posición está dentro de los límites del tablero.
        :param row: La fila a verificar.
        :param col: La columna a verificar.
        :return: True si está dentro del tablero, False si no.
        """
        return 0 <= row < 8 and 0 <= col < 8


