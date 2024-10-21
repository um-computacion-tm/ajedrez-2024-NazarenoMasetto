import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from juego.board import Board
from juego.pawn import Pawn
from juego.rook import Rook
from juego.king import King

class TestBoard(unittest.TestCase):
    def setUp(self):
        """ Configuración inicial para cada test. """
        self.board = Board()  # Inicializa un tablero

    def test_initial_board_setup(self):
        """ Verifica que el tablero se inicializa correctamente. """
        board = self.board.get_board()
        self.assertIsInstance(board[7][0], Rook)  # Torre blanca
        self.assertIsInstance(board[0][0], Rook)  # Torre negra
        self.assertIsInstance(board[6][4], Pawn)  # Peón blanco
        self.assertIsInstance(board[1][4], Pawn)  # Peón negro
        self.assertIsNone(board[4][4])  # Espacio vacío (debe ser None)

    def test_move_piece_valid(self):
        """ Verifica que una pieza se mueve correctamente de una posición a otra. """
        self.board.move_piece('e2', 'e4')  # Mueve el peón blanco de e2 a e4
        board = self.board.get_board()
        self.assertIsNone(board[6][4])  # La casilla e2 debe estar vacía (índice 6,4)
        self.assertIsInstance(board[4][4], Pawn)  # La casilla e4 debe tener un peón blanco (índice 4,4)

    def test_move_piece_invalid(self):
        """ Verifica que se lanza un error al intentar realizar un movimiento inválido. """
        with self.assertRaises(ValueError):
            self.board.move_piece('e2', 'e5')  # Movimiento inválido para un peón

    def test_move_piece_out_of_bounds(self):
        """ Verifica que se lanza un error al intentar mover fuera del tablero. """
        with self.assertRaises(ValueError):
            self.board.move_piece('e2', 'e9')  # Movimiento fuera del tablero

    def test_pawn_capture(self):
        """ Verifica que un peón pueda capturar una pieza en diagonal. """
        board = self.board.get_board()
        board[3][3] = Pawn("Black")  # Coloca un peón negro en d5 (índice 3,3)
        board[4][4] = Pawn("White")  # Coloca un peón blanco en e4 (índice 4,4)
        self.board.move_piece('e4', 'd5')  # Peón blanco captura peón negro en d5
        self.assertIsNone(board[4][4])  # La casilla e4 debe estar vacía
        self.assertIsInstance(board[3][3], Pawn)  # La casilla d5 debe tener un peón blanco

    def test_blocked_by_friendly_piece(self):
        """ Verifica que una pieza no puede moverse a una casilla ocupada por una pieza del mismo color. """
        with self.assertRaises(ValueError):
            self.board.move_piece('e2', 'e1')  # Movimiento inválido, bloqueado por una torre blanca

    def test_check_king_movement(self):
        """ Verifica que el rey se mueva correctamente. """
        board = self.board.get_board()
        board[4][4] = King("White")  # Coloca el rey blanco en e5 (índice 4,4)
        
        # Depuración: Ver el estado del tablero antes del movimiento
        print("Estado del tablero antes del movimiento del rey:")
        for row in board:
            print([str(piece) for piece in row])  # Mostrar el contenido de cada fila

        # Verificación explícita de la pieza en e5
        if not isinstance(board[4][4], King):
            raise AssertionError("El rey no está en la casilla e5 (índice 4,4)")
        
        # Depuración adicional para verificar la conversión de posición
        start_pos = self.board.position_to_indices('e5')
        print(f"Coordenadas convertidas de e5: {start_pos}")

        end_pos = self.board.position_to_indices('f4')
        print(f"Coordenadas convertidas de f4: {end_pos}")

        # Realizamos el movimiento
        self.board.move_piece('e5', 'f4')  # Mueve el rey de e5 a f4
        
        board = self.board.get_board()
        self.assertIsNone(board[4][4])  # La casilla e5 debe estar vacía
        self.assertIsInstance(board[3][5], King)  # La casilla f4 debe tener al rey blanco

if __name__ == '__main__':
    unittest.main()
