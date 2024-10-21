import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from juego.chess import Chess



class TestChess(unittest.TestCase):
    def setUp(self):
        self.game = Chess()

    def test_initial_turn(self):
        self.assertEqual(self.game.turn, "WHITE", "El turno inicial debe ser de las piezas blancas")

    def test_move_valid(self):
        # Mover un peón blanco de e2 a e4
        self.game.move(6, 4, 4, 4)  # e2 -> e4
        self.assertEqual(self.game.turn, "BLACK", "El turno debe cambiar a las piezas negras después de un movimiento válido")

    def test_move_invalid_out_of_bounds(self):
        with self.assertRaises(ValueError):
            self.game.move(8, 8, 9, 9)  # Movimiento fuera de los límites del tablero

    def test_move_invalid_no_piece(self):
        with self.assertRaises(ValueError):
            self.game.move(4, 4, 5, 5)  # Intentar mover desde una posición vacía

    def test_change_turn(self):
        # Mover un peón blanco de e2 a e4
        self.game.move(6, 4, 4, 4)  # e2 -> e4
        self.assertEqual(self.game.turn, "BLACK", "Después de mover debe ser el turno de las piezas negras")
        # Mover un peón negro de e7 a e5
        self.game.move(1, 4, 3, 4)  # e7 -> e5
        self.assertEqual(self.game.turn, "WHITE", "Después del turno de las piezas negras debe ser el turno de las blancas")

    def test_show_board(self):
        board_state = self.game.show_board()
        self.assertIsInstance(board_state, str, "El tablero debe devolverse como una cadena de texto")

if __name__ == '__main__':
    unittest.main()


