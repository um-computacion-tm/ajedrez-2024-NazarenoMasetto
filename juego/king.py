from juego.piece import Piece

class King(Piece):
    def __init__(self, color):
        """
        Constructor de la clase King. Llama al constructor de la clase base Piece.
        :param color: El color del rey ('White' o 'Black').
        """
        super().__init__(color)

    def valid_moves(self, current_position, board):
        """
        Calcula los movimientos válidos del rey según las reglas del ajedrez.
        El rey puede moverse una casilla en cualquier dirección.
        :param current_position: La posición actual del rey en coordenadas de matriz.
        :param board: El estado actual del tablero (lista de listas).
        :return: Una lista de posiciones válidas en formato (fila, columna) para mover el rey.
        """
        row, col = current_position
        moves = []

        # Definir las direcciones posibles del rey
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

        # Utilizar la función auxiliar para filtrar movimientos válidos
        moves = self._get_valid_moves(row, col, directions, board)

        return moves

    def _get_valid_moves(self, row, col, directions, board):
        """
        Función auxiliar que devuelve los movimientos válidos para una pieza en una dirección específica.
        :param row: La fila actual de la pieza.
        :param col: La columna actual de la pieza.
        :param directions: Lista de tuplas con las direcciones a verificar.
        :param board: El estado actual del tablero.
        :return: Lista de movimientos válidos en formato (fila, columna).
        """
        valid_moves = []
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if self._is_within_board(new_row, new_col) and self._can_move_to(new_row, new_col, board):
                valid_moves.append((new_row, new_col))
        return valid_moves

    def _is_within_board(self, row, col):
        """
        Verifica si una posición está dentro de los límites del tablero
        :param row: La fila a verificar.
        :param col: La columna a verificar.
        :return: True si la posición está dentro del tablero, False si no.
        """
        return 0 <= row < 8 and 0 <= col < 8

    def _can_move_to(self, row, col, board):
        """
        Verifica si la pieza se puede mover a una posición específica.
        :param row: La fila a verificar.
        :param col: La columna a verificar.
        :param board: El estado actual del tablero.
        :return: True si la casilla está vacía o contiene una pieza de color contrario.
        """
        target_piece = board[row][col]
        return target_piece == " " or target_piece.get_color() != self.get_color()

    def get_symbol(self):
        """
        Devuelve el símbolo que representa el rey en el tablero.
        'K' para rey blanco y 'k' para rey negro.
        :return: Un string con el símbolo del rey.
        """
        return "K" if self.get_color() == 'White' else "k"
