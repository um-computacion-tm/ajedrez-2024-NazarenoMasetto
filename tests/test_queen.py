import unittest
from juego.queen import Queen
from juego.board import Board

class TestQueen(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.queen = Queen('White')

    def test_valid_queen_moves(self):
        self.board.place_piece(self.queen, (4, 4))
        valid_moves = self.queen.valid_moves((4, 4), self.board.get_board())
        expected_moves = [
            (3, 3), (2, 2), (1, 1), (0, 0), (5, 5), (6, 6), (7, 7),
            (3, 5), (2, 6), (1, 7), (5, 3), (6, 2), (7, 1),
            (0, 4), (1, 4), (2, 4), (3, 4), (5, 4), (6, 4), (7, 4),
            (4, 0), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (4, 7)
        ]
        self.assertEqual(sorted(valid_moves), sorted(expected_moves))
