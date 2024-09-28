from abc import ABC, abstractmethod

class Piece(ABC):
    def __init__(self, color, board):
        """
        Constructor de la clase base Piece.
        :param color: El color de la pieza ('White' o 'Black').
        :param board: Referencia al tablero donde se juega.
        """
        self.__color__ = color
        self.__board__ = board  

    def get_color(self):
        """
        Devuelve el color de la pieza.
        :return: 'White' o 'Black', dependiendo del color de la pieza.
        """
        return self.__color__

    @abstractmethod
    def valid_moves(self, current_position):
        """
        Método abstracto que calcula los movimientos válidos de una pieza.
        Debe ser implementado por las subclases.
        """
        pass

    def get_moves_in_directions(self, current_position, directions):
        """
        Método auxiliar que calcula los movimientos válidos en una o varias direcciones.
        :param current_position: La posición actual de la pieza en coordenadas de matriz.
        :param directions: Una lista de tuplas que representan direcciones (dr, dc).
        :return: Una lista de posiciones válidas en formato (fila, columna) en esas direcciones.
        """
        row, col = current_position
        moves = []

        for dr, dc in directions:
            moves += self.__explore_direction(row, col, dr, dc)

        return moves

    def __explore_direction(self, row, col, dr, dc):
        """
        Explora una dirección específica y devuelve los movimientos válidos.
        :param row: Fila actual de la pieza.
        :param col: Columna actual de la pieza.
        :param dr: Dirección en la fila (desplazamiento).
        :param dc: Dirección en la columna (desplazamiento).
        :return: Lista de movimientos válidos en esa dirección.
        """
        moves = []
        new_row, new_col = row + dr, col + dc

        while self.__is_within_board(new_row, new_col):
            if self.__is_empty_square(new_row, new_col):
                moves.append((new_row, new_col))
            elif self.__can_capture(new_row, new_col):
                moves.append((new_row, new_col))
                break
            else:
                break
            new_row += dr
            new_col += dc

        return moves

    def __is_within_board(self, row, col):
        """
        Verifica si una casilla está dentro de los límites del tablero.
        :param row: Fila de la casilla.
        :param col: Columna de la casilla.
        :return: True si está dentro del tablero, False si no lo está.
        """
        return 0 <= row < 8 and 0 <= col < 8

    def __is_empty_square(self, row, col):
        """
        Verifica si una casilla está vacía.
        :param row: Fila de la casilla.
        :param col: Columna de la casilla.
        :return: True si la casilla está vacía, False si está ocupada.
        """
        return self.__board__[row][col] == " "

    def __can_capture(self, row, col):
        """
        Verifica si la pieza en una casilla es del color contrario y puede ser capturada.
        :param row: Fila de la casilla.
        :param col: Columna de la casilla.
        :return: True si la pieza puede ser capturada, False si no.
        """
        piece = self.__board__[row][col]
        return piece != " " and piece.get_color() != self.get_color()


# Clase SlidingPiece para piezas que se deslizan (torre, alfil, reina)
class SlidingPiece(Piece):
    def valid_moves(self, current_position, directions):
        """
        Calcula los movimientos válidos de una pieza deslizante (torre, alfil, reina)
        según las direcciones permitidas. Las direcciones se especifican en las subclases.
        :param current_position: La posición actual de la pieza.
        :param directions: Las direcciones en las que la pieza puede moverse.
        :return: Una lista de posiciones válidas.
        """
        return self.get_moves_in_directions(current_position, directions)


# Clase Rook 
class Rook(SlidingPiece):
    def valid_moves(self, current_position):
        """
        Movimientos válidos para la torre (vertical y horizontal).
        """
        directions = [
            (-1, 0), (1, 0),  # Movimientos verticales
            (0, -1), (0, 1)   # Movimientos horizontales
        ]
        return super().valid_moves(current_position, directions)

    def get_symbol(self):
        return "R" if self.get_color() == 'White' else "r"


# Clase Bishop 
class Bishop(SlidingPiece):
    def valid_moves(self, current_position):
        """
        Movimientos válidos para el alfil (diagonales).
        """
        directions = [
            (-1, -1), (-1, 1),  # Movimientos diagonales hacia arriba
            (1, -1), (1, 1)     # Movimientos diagonales hacia abajo
        ]
        return super().valid_moves(current_position, directions)

    def get_symbol(self):
        return "B" if self.get_color() == 'White' else "b"


# Clase Queen 
class Queen(SlidingPiece):
    def valid_moves(self, current_position):
        """
        Movimientos válidos para la reina (combinación de torre y alfil).
        """
        directions = [
            (-1, 0), (1, 0), (0, -1), (0, 1),  # Movimientos verticales y horizontales
            (-1, -1), (-1, 1), (1, -1), (1, 1)  # Movimientos diagonales
        ]
        return super().valid_moves(current_position, directions)

    def get_symbol(self):
        return "Q" if self.get_color() == 'White' else "q"


# Clase Knight 
class Knight(Piece):
    def valid_moves(self, current_position):
        """
        Calcula los movimientos válidos del caballo.
        El caballo se mueve en forma de "L".
        """
        row, col = current_position
        moves = []
        knight_moves = [
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)
        ]

        for dr, dc in knight_moves:
            new_row, new_col = row + dr, col + dc
            if self.__is_within_board(new_row, new_col):
                if self.__is_empty_square(new_row, new_col) or self.__can_capture(new_row, new_col):
                    moves.append((new_row, new_col))

        return moves

    def get_symbol(self):
        return "N" if self.get_color() == 'White' else "n"


# Clase Pawn 
class Pawn(Piece):
    def valid_moves(self, current_position):
        """
        Calcula los movimientos válidos del peón.
        El peón se mueve hacia adelante y captura en diagonal.
        """
        row, col = current_position
        moves = []
        direction = -1 if self.get_color() == 'White' else 1

        # Movimiento hacia adelante
        if self.__is_within_board(row + direction, col) and self.__is_empty_square(row + direction, col):
            moves.append((row + direction, col))

            # Primer movimiento: puede moverse 2 casillas
            if (self.get_color() == 'White' and row == 6) or (self.get_color() == 'Black' and row == 1):
                if self.__is_empty_square(row + 2 * direction, col):
                    moves.append((row + 2 * direction, col))

        # Captura diagonal izquierda
        if col - 1 >= 0 and self.__is_within_board(row + direction, col - 1) and self.__can_capture(row + direction, col - 1):
            moves.append((row + direction, col - 1))

        # Captura diagonal derecha
        if col + 1 < 8 and self.__is_within_board(row + direction, col + 1) and self.__can_capture(row + direction, col + 1):
            moves.append((row + direction, col + 1))

        return moves

    def get_symbol(self):
        return "P" if self.get_color() == 'White' else "p"


# Clase King 
class King(Piece):
    def valid_moves(self, current_position):
        """
        Calcula los movimientos válidos del rey.
        El rey se mueve una casilla en cualquier dirección.
        """
        row, col = current_position
        moves = []
        king_moves = [
            (-1, 0), (1, 0), (0, -1), (0, 1),
            (-1, -1), (-1, 1), (1, -1), (1, 1)
        ]

        for dr, dc in king_moves:
            new_row, new_col = row + dr, col + dc
            if self.__is_within_board(new_row, new_col):
                if self.__is_empty_square(new_row, new_col) or self.__can_capture(new_row, new_col):
                    moves.append((new_row, new_col))

        return moves

    def get_symbol(self):
        return "K" if self.get_color() == 'White' else "k"

