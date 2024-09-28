from abc import ABC, abstractmethod

class Piece(ABC):
    def __init__(self, color):
       
        self.__color__ = color

    def get_color(self):
        
        return self.__color__

    @abstractmethod
    def valid_moves(self, current_position, board):
       
        pass

    @abstractmethod
    def get_symbol(self):
       
        pass

    def __str__(self):
        
        return self.get_symbol()

    def get_moves_in_directions(self, current_position, board, directions):
        
        row, col = current_position
        moves = []

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            # Continuar en una dirección hasta que encontremos un borde del tablero o una pieza
            while 0 <= new_row < 8 and 0 <= new_col < 8:
                if board[new_row][new_col] == " ":
                    moves.append((new_row, new_col))  # Casilla vacía, movimiento válido
                elif board[new_row][new_col].get_color() != self.get_color():
                    moves.append((new_row, new_col))  # Captura válida
                    break  # Detener después de capturar
                else:
                    break  # No puede moverse más allá de una pieza del mismo color
                new_row += dr
                new_col += dc

        return moves
