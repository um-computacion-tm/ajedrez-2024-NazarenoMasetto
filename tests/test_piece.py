import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from juego.piece import Piece

class TestPiece(unittest.TestCase):
    def setUp(self):
        """ Configuración inicial para cada test. """
        self.piece = Piece("White")  # Pieza de prueba que no debería ser instanciada directamente
        # Un tablero vacío de 8x8
        self.empty_board = [[None for _ in range(8)] for _ in range(8)]

    def test_get_color(self):
        """ Verifica que el color de la pieza se obtenga correctamente. """
        self.assertEqual(self.piece.get_color(), "White")

    def test_abstract_methods(self):
        """ Verifica que los métodos abstractos lancen NotImplementedError. """
        with self.assertRaises(NotImplementedError):
            self.piece.valid_moves((0, 0), self.empty_board)
        with self.assertRaises(NotImplementedError):
            self.piece.get_symbol()

    def test_is_within_board(self):
        """ Verifica que los movimientos dentro y fuera del tablero se detecten correctamente. """
        self.assertTrue(self.piece._is_within_board(0, 0))  # Esquina inferior izquierda
        self.assertTrue(self.piece._is_within_board(7, 7))  # Esquina superior derecha
        self.assertFalse(self.piece._is_within_board(8, 0))  # Fuera del tablero (fila)
        self.assertFalse(self.piece._is_within_board(0, 8))  # Fuera del tablero (columna)

    def test_calculate_new_position(self):
        """ Verifica que las nuevas posiciones se calculen correctamente. """
        self.assertEqual(self.piece._calculate_new_position(4, 4, (1, 0)), (5, 4))  # Movimiento hacia abajo
        self.assertEqual(self.piece._calculate_new_position(4, 4, (-1, 0)), (3, 4))  # Movimiento hacia arriba
        self.assertEqual(self.piece._calculate_new_position(4, 4, (0, 1)), (4, 5))  # Movimiento hacia la derecha
        self.assertEqual(self.piece._calculate_new_position(4, 4, (0, -1)), (4, 3))  # Movimiento hacia la izquierda

    def test_can_move_to_empty_square(self):
        """ Verifica que una pieza pueda moverse a una casilla vacía. """
        self.assertTrue(self.piece._can_move_to(4, 4, self.empty_board))  # La casilla está vacía (None)

    def test_can_move_to_enemy_square(self):
        """ Verifica que una pieza pueda moverse a una casilla ocupada por una pieza enemiga. """
        self.empty_board[4][4] = Piece("Black")  # Casilla ocupada por una pieza enemiga
        self.assertTrue(self.piece._can_move_to(4, 4, self.empty_board))

    def test_cannot_move_to_friendly_square(self):
        """ Verifica que una pieza no pueda moverse a una casilla ocupada por una pieza amiga. """
        self.empty_board[4][4] = Piece("White")  # Casilla ocupada por una pieza amiga
        self.assertFalse(self.piece._can_move_to(4, 4, self.empty_board))

if __name__ == '__main__':
    unittest.main()
