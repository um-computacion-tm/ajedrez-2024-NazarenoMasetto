from juego.pawn import Pawn
from juego.rook import Rook
from juego.bishop import Bishop
from juego.knight import Knight
from juego.queen import Queen
from juego.king import King
from juego.piece import Piece

class Board:
    def __init__(self):
        self.__board__ = self.__initialize_board__()

    def __initialize_board__(self):
        """ Inicializa el tablero con las piezas en sus posiciones iniciales. """
        board = [[None for _ in range(8)] for _ in range(8)]  # Usa None para casillas vacías
        self.__initialize_pieces(board, "White", 7, 6)  # Blancas en filas 7 y 6
        self.__initialize_pieces(board, "Black", 0, 1)  # Negras en filas 0 y 1
        return board

    def __initialize_pieces(self, board, color, back_row, pawn_row):
        """ Inicializa las piezas en el tablero. """
        board[back_row] = [Rook(color), Knight(color), Bishop(color), Queen(color),
                           King(color), Bishop(color), Knight(color), Rook(color)]
        board[pawn_row] = [Pawn(color) for _ in range(8)]

    def get_board(self):
        """ Devuelve el estado actual del tablero. """
        return self.__board__

    def move_piece(self, start_pos, end_pos):
        """
        Mueve una pieza desde la posición inicial a la final.
        :param start_pos: La posición inicial en notación algebraica o en formato (fila, columna).
        :param end_pos: La posición final en notación algebraica o en formato (fila, columna).
        """
        # Si las posiciones están en notación algebraica, conviértalas a índices
        if isinstance(start_pos, str):
            start_pos = self.position_to_indices(start_pos)
        if isinstance(end_pos, str):
            end_pos = self.position_to_indices(end_pos)

        start_row, start_col = start_pos
        end_row, end_col = end_pos

        piece = self.get_piece_at(start_pos)
        
        if not piece:
            raise ValueError("No hay ninguna pieza en la posición de inicio")
        
        if not self.is_valid_move(piece, start_pos, end_pos):
            raise ValueError("Movimiento no permitido para la pieza seleccionada")
        
        self.perform_move(piece, start_pos, end_pos)

    def get_piece_at(self, pos):
        """
        Devuelve la pieza en una posición específica del tablero.
        :param pos: Una tupla con la posición (fila, columna).
        :return: La pieza en esa posición o None si no hay pieza.
        """
        row, col = pos
        return self.__board__[row][col]

    def is_valid_move(self, piece, start_pos, end_pos):
        """
        Verifica si el movimiento es válido para la pieza seleccionada.
        :param piece: La pieza que se está moviendo.
        :param start_pos: Una tupla con la posición de inicio (fila, columna).
        :param end_pos: Una tupla con la posición final (fila, columna).
        :return: True si el movimiento es válido, False en caso contrario.
        """
        start_row, start_col = start_pos
        end_row, end_col = end_pos
        
        valid_moves = piece.valid_moves(start_pos, self.__board__)
        return (end_row, end_col) in valid_moves and \
               (self.__board__[end_row][end_col] is None or
                self.__board__[end_row][end_col].get_color() != piece.get_color())

    def perform_move(self, piece, start_pos, end_pos):
        """
        Realiza el movimiento de la pieza en el tablero.
        :param piece: La pieza que se está moviendo.
        :param start_pos: Una tupla con la posición de inicio (fila, columna).
        :param end_pos: Una tupla con la posición final (fila, columna).
        """
        start_row, start_col = start_pos
        end_row, end_col = end_pos
        
        self.__board__[end_row][end_col] = piece
        self.__board__[start_row][start_col] = None

    @staticmethod
    def position_to_indices(pos):
        """
        Convierte una posición en formato de ajedrez (e.g., "e2") en índices de matriz.
        :param pos: La posición en notación algebraica (ejemplo: 'e2').
        :return: Una tupla (fila, columna) correspondiente a los índices en la matriz.
        """
        col = ord(pos[0]) - ord('a')
        row = 8 - int(pos[1])
        return row, col
