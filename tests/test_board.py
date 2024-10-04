import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from juego.board import Board
from juego.pawn import Pawn
from juego.piece import Piece
class TestBoard(unittest.TestCase):
    def setUp(self):
        """ Configura el entorno para cada prueba, inicializando un tablero nuevo. """
        self.board = Board()
    def test_initial_board_setup(self):
        """ Verifica que el tablero se inicializa correctamente con las piezas en sus posiciones iniciales. """
        board_state = self.board.get_board()
        # Verifica peones blancos en la fila 6
        for col in range(8):
            piece = board_state[6][col]
            self.assertIsInstance(piece, Pawn)
            self.assertEqual(piece.get_color(), 'White')
        # Verifica peones negros en la fila 1
        for col in range(8):
            piece = board_state[1][col]
            self.assertIsInstance(piece, Pawn)
            self.assertEqual(piece.get_color(), 'Black')
    def test_move_piece_valid(self):
        """ Verifica que una pieza se mueve correctamente de una posición a otra. """
        self.board.move_piece("e2", "e4")
        moved_piece = self.board.get_piece_at((4, 4))
        self.assertIsInstance(moved_piece, Piece)
        self.assertEqual(moved_piece.get_color(), 'White')
        # Verifica que la posición original está vacía
        self.assertIsNone(self.board.get_piece_at((6, 4)))
    def test_move_piece_invalid(self):
        """ Verifica que un movimiento inválido arroja una excepción. """
        with self.assertRaises(ValueError):
            self.board.move_piece("e2", "e5")  # Movimiento inválido para un peón
    def test_pawn_capture(self):
        """ Verifica que un peón puede capturar una pieza en diagonal. """
        # Coloca un peón negro en una posición capturable
        self.board.get_board()[5][3] = Pawn("Black")
        # Mueve el peón blanco de e2 a d3 para capturar
        self.board.move_piece("e2", "d3")
        moved_pawn = self.board.get_piece_at((5, 3))
        self.assertIsInstance(moved_pawn, Pawn)
        self.assertEqual(moved_pawn.get_color(), 'White')
        # Verifica que la posición original está vacía
        self.assertIsNone(self.board.get_piece_at((6, 4)))
    def test_position_to_indices(self):
        """ Verifica que las posiciones en notación algebraica se convierten correctamente a índices de matriz. """
        self.assertEqual(self.board.position_to_indices("e2"), (6, 4))
        self.assertEqual(self.board.position_to_indices("a1"), (7, 0))
        self.assertEqual(self.board.position_to_indices("h8"), (0, 7))
    def test_invalid_start_position(self):
        """ Verifica que se arroja un error cuando no hay pieza en la posición inicial. """
        with self.assertRaises(ValueError):
            self.board.move_piece("e3", "e4")  # No hay pieza en e3
    def test_invalid_end_position(self):
        """ Verifica que se arroja un error cuando el movimiento no es válido para la pieza. """
        with self.assertRaises(ValueError):
            self.board.move_piece("e2", "e5")  # Movimiento inválido para el peón blanco
    def test_perform_move(self):
        """ Verifica que el método perform_move mueve una pieza correctamente. """
        pawn = Pawn("White")
        self.board.get_board()[6][4] = pawn
        self.board.perform_move(pawn, (6, 4), (4, 4))
        # Verifica que el peón fue movido
        self.assertIsNone(self.board.get_piece_at((6, 4)))
        self.assertEqual(self.board.get_piece_at((4, 4)), pawn)
if __name__ == '__main__':
    unittest.main()