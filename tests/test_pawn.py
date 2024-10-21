import unittest
from juego.pawn import Pawn
from juego.board import Board

class TestPawn(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.pawn_white = Pawn('White')

    def test_pawn_valid_moves(self):
        """Verifica los movimientos válidos del peón."""
        self.board.place_piece(self.pawn_white, (6, 4))  # Peón blanco en e2
        valid_moves = self.pawn_white.valid_moves((6, 4), self.board.get_board())
        expected_moves = [(5, 4), (4, 4)]  # Puede avanzar una o dos casillas
        self.assertEqual(sorted(valid_moves), sorted(expected_moves))

    def test_pawn_blocked_by_same_color(self):
        """Verifica que el peón no puede moverse si está bloqueado por otra pieza del mismo color."""
        self.board.place_piece(self.pawn_white, (6, 4))
        self.board.place_piece(Pawn('White'), (5, 4))  # Bloqueado por otro peón blanco
        valid_moves = self.pawn_white.valid_moves((6, 4), self.board.get_board())
        self.assertEqual(valid_moves, [])  # No debe haber movimientos válidos

    def test_pawn_capture_opponent(self):
        """Verifica que el peón puede capturar una pieza enemiga en diagonal."""
        self.board.place_piece(self.pawn_white, (6, 4))
        self.board.place_piece(Pawn('Black'), (5, 5))  # Peón enemigo en f3
        valid_moves = self.pawn_white.valid_moves((6, 4), self.board.get_board())
        self.assertIn((5, 5), valid_moves)  # Puede capturar en diagonal

    def test_pawn_double_advance_blocked(self):
        """Verifica que el peón no puede avanzar dos casillas si la primera está bloqueada."""
        self.board.place_piece(self.pawn_white, (6, 4))
        self.board.place_piece(Pawn('Black'), (5, 4))  # Bloqueado en e3
        valid_moves = self.pawn_white.valid_moves((6, 4), self.board.get_board())
        self.assertNotIn((4, 4), valid_moves)  # No debería poder avanzar dos casillas

if __name__ == '__main__':
    unittest.main()
