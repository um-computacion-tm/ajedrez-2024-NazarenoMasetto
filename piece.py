from abc import ABC, abstractmethod

class Piece(ABC):
    def __init__(self, color, board):
        self.__color__ = color
        self.__board__ = board  # El tablero se almacena como un atributo de instancia.

    def get_color(self):
        return self.__color__

    @abstractmethod
    def valid_moves(self, current_position):
        pass

    def get_moves_in_directions(self, current_position, directions):
        row, col = current_position
        moves = []

        for dr, dc in directions:
            moves += self.__explore_direction(row, col, dr, dc)

        return moves

    def __explore_direction(self, row, col, dr, dc):
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
        return 0 <= row < 8 and 0 <= col < 8

    def __is_empty_square(self, row, col):
        return self.__board__[row][col] == " "

    def __can_capture(self, row, col):
        piece = self.__board__[row][col]
        return piece != " " and piece.get_color() != self.get_color()


class Queen(Piece):
    def valid_moves(self, current_position):
        directions = [
            (-1, 0), (1, 0), (0, -1), (0, 1),  # Movimientos verticales y horizontales
            (-1, -1), (-1, 1), (1, -1), (1, 1)  # Movimientos diagonales
        ]
        return self.get_moves_in_directions(current_position, directions)

    def get_symbol(self):
        return "Q" if self.get_color() == 'White' else "q"


class Rook(Piece):
    def valid_moves(self, current_position):
        directions = [
            (-1, 0), (1, 0), (0, -1), (0, 1)  # Movimientos verticales y horizontales
        ]
        return self.get_moves_in_directions(current_position, directions)

    def get_symbol(self):
        return "R" if self.get_color() == 'White' else "r"


class Bishop(Piece):
    def valid_moves(self, current_position):
        directions = [
            (-1, -1), (-1, 1), (1, -1), (1, 1)  # Movimientos diagonales
        ]
        return self.get_moves_in_directions(current_position, directions)

    def get_symbol(self):
        return "B" if self.get_color() == 'White' else "b"
