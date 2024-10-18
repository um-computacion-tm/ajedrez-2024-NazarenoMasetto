from juego.piece import Piece
class Knight(Piece):
    def __init__(self, color):
        """
        Constructor de la clase Knight.
        :param color: El color de la pieza ('White' o 'Black').
        """
        super().__init__(color)

    def get_symbol(self):
        """
        Devuelve el símbolo que representa al caballo.
        :return: 'N' para el caballo.
        """
        return 'N'

    def valid_moves(self, current_position, board):
        """
        Calcula los movimientos válidos para el caballo desde la posición actual.
        :param current_position: Tupla (fila, columna) representando la posición actual del caballo.
        :param board: El estado actual del tablero como una lista de listas.
        :return: Lista de posiciones válidas a las que el caballo puede moverse.
        """
        row, col = current_position
        possible_moves = self._get_knight_moves()
        valid_moves = []

        for move in possible_moves:
            new_row, new_col = row + move[0], col + move[1]
            if self._is_within_board(new_row, new_col) and self._can_move_to(new_row, new_col, board):
                valid_moves.append((new_row, new_col))

        return valid_moves

    @staticmethod
    def _get_knight_moves():
        """
        Devuelve los posibles movimientos relativos del caballo.
        :return: Lista de tuplas con los movimientos posibles del caballo.
        """
        return [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

    @staticmethod
    def _is_within_board(row, col):
        """
        Verifica si la posición está dentro de los límites del tablero.
        :param row: Fila de la posición.
        :param col: Columna de la posición.
        :return: True si la posición está dentro del tablero, False en caso contrario.
        """
        return 0 <= row < 8 and 0 <= col < 8

    def _can_move_to(self, row, col, board):
        """
        Verifica si el caballo puede moverse a la posición especificada.
        :param row: Fila de destino.
        :param col: Columna de destino.
        :param board: El estado actual del tablero.
        :return: True si el movimiento es válido, False en caso contrario.
        """
        target_piece = board[row][col]
        return target_piece is None or target_piece.get_color() != self.get_color()
