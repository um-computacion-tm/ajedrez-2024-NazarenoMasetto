import unittest
from juego.piece import Piece

class TestPiece(Piece):
    def __init__(self, color):
        super().__init__(color)

    def valid_moves(self, current_position, board):
        return [(current_position[0] + 1, current_position[1])]

    def get_symbol(self):
        return 'P'

class TestPieceClass(unittest.TestCase):
    def setUp(self):
        self.white_piece = TestPiece('White')
        self.black_piece = TestPiece('Black')

    def test_get_color(self):
        self.assertEqual(self.white_piece.get_color(), 'White')
        self.assertEqual(self.black_piece.get_color(), 'Black')

    def test_valid_moves(self):
        current_position = (3, 3)
        expected_moves = [(4, 3)]
        self.assertEqual(self.white_piece.valid_moves(current_position, None), expected_moves)

    def test_get_symbol(self):
        self.assertEqual(self.white_piece.get_symbol(), 'P')

    def test_invalid_color(self):
        with self.assertRaises(ValueError):
            Piece('InvalidColor')

if __name__ == '__main__':
    unittest.main()
