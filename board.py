from pawn import Pawn
from rook import Rook
from bishop import Bishop
from knight import Knight
from queen import Queen
from king import King
from piece import Piece

class Board:
    def __init__(self):
        
        self.__board__ = self.__initialize_board__()

    def __initialize_board__(self):
       
        board = [[" " for _ in range(8)] for _ in range(8)]
        
        # Piezas blancas
        board[0] = [
            Rook("White"), Knight("White"), Bishop("White"), Queen("White"),
            King("White"), Bishop("White"), Knight("White"), Rook("White")
        ]
        board[1] = [Pawn("White") for _ in range(8)]
        
        # Piezas negras
        board[6] = [Pawn("Black") for _ in range(8)]
        board[7] = [
            Rook("Black"), Knight("Black"), Bishop("Black"), Queen("Black"),
            King("Black"), Bishop("Black"), Knight("Black"), Rook("Black")
        ]
        
        return board

    def move_piece(self, start, end):
       
        start_row, start_col = self.position_to_indices(start)
        end_row, end_col = self.position_to_indices(end)
        
        # Obtener la pieza en la posición inicial
        piece = self.__board__[start_row][start_col]
        
        if isinstance(piece, Piece):
            valid_moves = piece.valid_moves((start_row, start_col), self.__board__)
            
            # Verificar si el movimiento es válido
            if (end_row, end_col) in valid_moves:
                # Verificar si la casilla final está vacía o contiene una pieza del color opuesto
                if self.__board__[end_row][end_col] == " " or self.__board__[end_row][end_col].__color__ != piece.__color__:
                    self.__board__[end_row][end_col] = piece
                    self.__board__[start_row][start_col] = " "
                else:
                    raise ValueError("Movimiento inválido: la casilla está ocupada por una pieza del mismo color")
            else:
                raise ValueError("Movimiento no permitido para la pieza seleccionada")
        else:
            raise ValueError("No hay ninguna pieza en la posición de inicio")

    @staticmethod
    def position_to_indices(pos):
        
        col = ord(pos[0]) - ord('a')
        row = 8 - int(pos[1])
        return row, col
