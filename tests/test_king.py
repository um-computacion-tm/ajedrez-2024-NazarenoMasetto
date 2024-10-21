import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from juego.king import King
from juego.piece import Piece

class TestKing(unittest.TestCase):
    def setUp(self):
        """ Configuración inicial para cada test. """
        self.king_white = King("White")
        self.king_black = King("Black")
        # Un tablero vacío de 8x8
        self.empty_board = [[None for _ in range(8)] for _ in range(8)]

    def test_king_symbol(self):
        """ Verifica que el símbolo del rey sea correcto. """
        self.assertEqual(self.king_white.get_symbol(), 'K')
        self.assertEqual(self.king_black.get_symbol(), 'k')

    def test_king_valid_moves(self):
        """ Verifica que los movimientos válidos del rey sean correctos. """
        # Posición central, rey blanco en e4
        current_position = (4, 4)
        expected_moves = [
            (4, 5), (5, 4), (4, 3), (3, 4),  # Movimientos ortogonales
            (5, 5), (5, 3), (3, 5), (3, 3)   # Movimientos diagonales
        ]
        valid_moves = self.king_white.valid_moves(current_position, self.empty_board)
        self.assertEqual(sorted(valid_moves), sorted(expected_moves))

    def test_king_blocked_by_friendly_pieces(self):
        """ Verifica que el rey no pueda moverse a una casilla ocupada por una pieza del mismo color. """
        # Colocamos algunas piezas blancas alrededor del rey
        self.empty_board[5][4] = Piece("White")
        self.empty_board[4][5] = Piece("White")
        current_position = (4, 4)
        expected_moves = [
            (4, 3), (3, 4), (5, 5), (5, 3), (3, 5), (3, 3)
        ]  # Movimientos sin las posiciones ocupadas por piezas blancas
        valid_moves = self.king_white.valid_moves(current_position, self.empty_board)
        self.assertEqual(sorted(valid_moves), sorted(expected_moves))

    def test_king_capture_opponent_pieces(self):
        """ Verifica que el rey pueda capturar piezas enemigas. """
        # Colocamos algunas piezas negras alrededor del rey blanco
        self.empty_board[5][4] = Piece("Black")
        self.empty_board[4][5] = Piece("Black")
        current_position = (4, 4)
        expected_moves = [
            (4, 3), (3, 4), (5, 4), (4, 5), (5, 5), (5, 3), (3, 5), (3, 3)
        ]  # Movimientos más las posiciones con piezas negras capturables
        valid_moves = self.king_white.valid_moves(current_position, self.empty_board)
        self.assertEqual(sorted(valid_moves), sorted(expected_moves))

if __name__ == '__main__':
    unittest.main()
