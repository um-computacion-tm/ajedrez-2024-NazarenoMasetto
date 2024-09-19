import unittest
from piece import Piece


class Bishop(Piece):
    def valid_moves(self, position, board=None):
        row, col = position
        moves = [(row + i, col + i) for i in range(-7, 8) if 0 <= row + i < 8 and 0 <= col + i < 8 and i != 0] + \
                [(row + i, col - i) for i in range(-7, 8) if 0 <= row + i < 8 and 0 <= col - i < 8 and i != 0]
        return moves

class TestBishop(unittest.TestCase):
    def setUp(self):
        
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.bishop = Bishop()

    def test_center_position(self):
        
        expected_moves = [
            (5, 5), (6, 6), (7, 7), (3, 3), (2, 2), (1, 1), (0, 0),  
            (5, 3), (6, 2), (7, 1), (3, 5), (2, 6), (1, 7)  
        ]
        self.assertCountEqual(self.bishop.valid_moves((4, 4), self.board), expected_moves)

    def test_corner_position(self):
        
        expected_moves = [
            (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7)  
        ]
        self.assertCountEqual(self.bishop.valid_moves((0, 0), self.board), expected_moves)

    def test_edge_position(self):
        
        expected_moves = [
            (1, 3), (2, 4), (3, 5), (4, 6), (5, 7),  
            (1, 1), (2, 0)  
        ]
        self.assertCountEqual(self.bishop.valid_moves((0, 2), self.board), expected_moves)

if __name__ == '__main__':
    unittest.main()
