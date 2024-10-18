import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from juego.chess import Chess
from juego.piece import Piece
class TestChess(unittest.TestCase):
    def setUp(self):
        self.chess_game = Chess()
    def test_initial_turn(self):
        """Test para verificar que el turno inicial es de las blancas."""
        self.assertEqual(self.chess_game.turn, "WHITE")
    def test_switch_turn(self):
        """Test para cambiar el turno después de un movimiento."""
        self.chess_game.change_turn()
        self.assertEqual(self.chess_game.turn, "BLACK")
        self.chess_game.change_turn()
        self.assertEqual(self.chess_game.turn, "WHITE")
    def test_move_piece(self):
        """Test para mover una pieza en el tablero."""
        # Colocar una pieza en el tablero
        self.chess_game.board.set_piece(0, 0, Piece("WHITE"))
        # Realizar el movimiento de la pieza blanca
        self.chess_game.move(0, 0, 2, 2)
        self.assertIsNone(self.chess_game.board.get_piece(0, 0))  # La posición original debe estar vacía
        self.assertIsNotNone(self.chess_game.board.get_piece(2, 2))  # La nueva posición debe tener la pieza
    def test_invalid_move_out_of_bounds(self):
        """Test para verificar que no se puede mover una pieza fuera del tablero."""
        self.chess_game.board.set_piece(0, 0, Piece("WHITE"))
        with self.assertRaises(ValueError):
            self.chess_game.move(0, 0, 8, 8)  # Fuera de los límites del tablero
    def test_invalid_turn(self):
        """Test para verificar que no se puede mover una pieza que no corresponde al turno."""
        self.chess_game.board.set_piece(0, 0, Piece("WHITE"))
        self.chess_game.board.set_piece(1, 1, Piece("BLACK"))
        # Cambiamos el turno a las negras
        self.chess_game.change_turn()
        with self.assertRaises(ValueError):
            self.chess_game.move(0, 0, 2, 2)  # Intentamos mover la pieza blanca en el turno de las negras
    def test_piece_not_found(self):
        """Test para verificar que no se puede mover desde una posición vacía."""
        with self.assertRaises(ValueError):
            self.chess_game.move(0, 0, 2, 2)  # No hay ninguna pieza en la posición (0, 0)
if __name__ == '__main__':
    unittest.main()