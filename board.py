from pawn import Pawn
from rook import Rook
from bishop import Bishop
from knight import Knight
from queen import Queen
from king import King
from piece import Piece

class Board:
    def __init__(self):
        """
        Constructor de la clase Board. Inicializa el tablero con las piezas en sus posiciones iniciales.
        """
        self.__board__ = self.__initialize_board__()

    def __initialize_board__(self):
        """
        Inicializa el tablero de ajedrez con la disposición estándar de piezas.
        :return: Una lista de listas (8x8) que representa el tablero de ajedrez.
        """
        board = [[" " for _ in range(8)] for _ in range(8)]
        
        # Inicializar filas de piezas principales y peones
        self.__initialize_pieces(board, "White", 0, 1)
        self.__initialize_pieces(board, "Black", 7, 6)

        return board

    def __initialize_pieces(self, board, color, back_row, pawn_row):
        """
        Inicializa las piezas para un color dado en las filas correspondientes.
        :param board: El tablero de ajedrez a inicializar.
        :param color: El color de las piezas ("White" o "Black").
        :param back_row: La fila donde se colocan las piezas principales (torre, caballo, etc.).
        :param pawn_row: La fila donde se colocan los peones.
        """
        # Piezas principales
        board[back_row] = [
            Rook(color), Knight(color), Bishop(color), Queen(color),
            King(color), Bishop(color), Knight(color), Rook(color)
        ]
        # Peones
        board[pawn_row] = [Pawn(color) for _ in range(8)]

    def move_piece(self, start, end):
        """
        Mueve una pieza desde la posición inicial a la final, si el movimiento es válido.
        :param start: La posición inicial en formato de ajedrez (e.g., "e2").
        :param end: La posición final en formato de ajedrez (e.g., "e4").
        :raises ValueError: Si el movimiento no es válido o no hay pieza en la posición de inicio.
        """
        start_row, start_col = self.position_to_indices(start)
        end_row, end_col = self.position_to_indices(end)
        
        piece = self.get_piece_at(start_row, start_col)
        
        if not piece:
            raise ValueError("No hay ninguna pieza en la posición de inicio")
        
        if not self.is_valid_move(piece, start_row, start_col, end_row, end_col):
            raise ValueError("Movimiento no permitido para la pieza seleccionada")
        
        self.perform_move(piece, start_row, start_col, end_row, end_col)

    def get_piece_at(self, row, col):
        """
        Devuelve la pieza en una posición específica del tablero.
        """
        piece = self.__board__[row][col]
        return piece if isinstance(piece, Piece) else None

    def is_valid_move(self, piece, start_row, start_col, end_row, end_col):
        """
        Verifica si el movimiento es válido para la pieza seleccionada.
        """
        valid_moves = piece.valid_moves((start_row, start_col), self.__board__)
        return (end_row, end_col) in valid_moves and \
               (self.__board__[end_row][end_col] == " " or
                self.__board__[end_row][end_col].__color__ != piece.__color__)

    def perform_move(self, piece, start_row, start_col, end_row, end_col):
        """
        Realiza el movimiento de la pieza en el tablero.
        """
        self.__board__[end_row][end_col] = piece
        self.__board__[start_row][start_col] = " "

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
