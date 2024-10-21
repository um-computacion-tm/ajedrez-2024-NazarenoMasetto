import unittest
from juego.rook import Rook
from juego.board import Board

class TestRook(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.rook = Rook('White')

    def test_valid_rook_moves(self):
        self.board.place_piece(self.rook, (4, 4))
        valid_moves = self.rook.valid_moves((4, 4), self.board.get_board())
        expected_moves = [(0, 4), (1, 4), (2, 4), (3, 4), (5, 4), (6, 4), (7, 4), (4, 0), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (4, 7)]
        self.assertEqual(sorted(valid_moves), sorted(expected_moves))
