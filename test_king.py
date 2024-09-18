import unittest
from king import King

class TestKingMoves(unittest.TestCase):
    def test_valid_moves_center(self):
        king = King()
        position = (4, 4)
        board = [[0]*8 for _ in range(8)]
        expected_moves = [(3, 3), (3, 4), (3, 5), (4, 3), (4, 5), (5, 3), (5, 4), (5, 5)]
        self.assertEqual(king.valid_moves(position, board), expected_moves)

    def test_valid_moves_corner(self):
        king = King()
        position = (0, 0)
        board = [[0]*8 for _ in range(8)]
        expected_moves = [(0, 1), (1, 0), (1, 1)]
        self.assertEqual(king.valid_moves(position, board), expected_moves)

    def test_valid_moves_edge(self):
        king = King()
        position = (0, 4)
        board = [[0]*8 for _ in range(8)]
        expected_moves = [(0, 3), (0, 5), (1, 3), (1, 4), (1, 5)]
        self.assertEqual(king.valid_moves(position, board), expected_moves)

    def test_invalid_moves_out_of_board(self):
        king = King()
        position = (8, 8)
        board = [[0]*8 for _ in range(8)]
        expected_moves = []
        self.assertEqual(king.valid_moves(position, board), expected_moves)

if __name__ == '__main__':
    unittest.main()