import unittest
from juego.bishop import Bishop
from juego.board import Board

class TestBishop(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.bishop = Bishop('White')

    def test_valid_bishop_moves(self):
        self.board.place_piece(self.bishop, (4, 4))
        valid_moves = self.bishop.valid_moves((4, 4), self.board.get_board())
        expected_moves = [(3, 3), (2, 2), (1, 1), (0, 0), (5, 5), (6, 6), (7, 7), (3, 5), (2, 6), (1, 7), (5, 3), (6, 2), (7, 1)]
        self.assertEqual(sorted(valid_moves), sorted(expected_moves))
