import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from juego.chess import Chess
from juego.pawn import Pawn

class TestChess(unittest.TestCase):

    def setUp(self):
        self.game = Chess()

    def test_move_valid(self):
        """Verifica que un movimiento válido se procese correctamente."""
        self.game.move(6, 4, 4, 4)  # e2 -> e4
        board = self.game.get_board()
        self.assertEqual(board[6][4], " ")  # La casilla de origen debe estar vacía
        self.assertIsInstance(board[4][4], Pawn)  # La casilla de destino debe tener un peón blanco

    def test_move_invalid_no_piece(self):
        """Verifica que intentar mover una pieza desde una casilla vacía arroje un error."""
        with self.assertRaises(ValueError):
            self.game.move(4, 4, 5, 5)  # No hay pieza en e3 (4,4)

    def test_change_turn(self):
        """Verifica que el turno cambie correctamente después de un movimiento válido."""
        self.game.move(6, 4, 4, 4)  # e2 -> e4
        self.assertEqual(self.game.turn, "BLACK")
        self.game.move(1, 4, 3, 4)  # e7 -> e5
        self.assertEqual(self.game.turn, "WHITE")

if __name__ == '__main__':
    unittest.main()

if __name__ == '__main__':
    unittest.main()


