import unittest
from juego.knight import Knight
from juego.board import Board

class TestKnight(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.knight_white = Knight('White')

    def test_knight_valid_moves(self):
        """Verifica los movimientos válidos del caballo."""
        self.board.place_piece(self.knight_white, (4, 4))
        valid_moves = self.knight_white.valid_moves((4, 4), self.board.get_board())
        expected_moves = [(2, 3), (2, 5), (3, 2), (3, 6), (5, 2), (5, 6), (6, 3), (6, 5)]
        self.assertEqual(sorted(valid_moves), sorted(expected_moves))

    def test_knight_blocked_by_same_color(self):
        """Verifica que el caballo no puede capturar piezas del mismo color."""
        self.board.place_piece(self.knight_white, (4, 4))
        self.board.place_piece(Knight('White'), (6, 5))  # Bloqueado por otro caballo blanco
        valid_moves = self.knight_white.valid_moves((4, 4), self.board.get_board())
        self.assertNotIn((6, 5), valid_moves)  # No debería poder capturar

    def test_knight_capture_opponent(self):
        """Verifica que el caballo puede capturar piezas enemigas."""
        self.board.place_piece(self.knight_white, (4, 4))
        self.board.place_piece(Knight('Black'), (6, 5))  # Caballo enemigo
        valid_moves = self.knight_white.valid_moves((4, 4), self.board.get_board())
        self.assertIn((6, 5), valid_moves)  # Debería poder capturar

if __name__ == '__main__':
    unittest.main()
