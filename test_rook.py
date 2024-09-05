import unittest
from rook import Rook
from board import Board

class TestRook(unittest.TestCase):
    def setUp(self):
        self.board = Board()  
        self.rook_white = Rook("white", self.board)
        self.rook_black = Rook("black", self.board)

    def test_valid_positions(self):
        self.rook_white.board.set_piece(3, 3, self.rook_white)
        for i in range(4, 8):
            self.assertTrue(self.rook_white.valid_positions(3, 3, i, 3))

        self.rook_white.board.set_piece(5, 3, self.rook_white)
        for i in range(4, -1, -1):
            self.assertTrue(self.rook_white.valid_positions(5, 3, i, 3))

        self.rook_white.board.set_piece(3, 3, self.rook_white)
        for i in range(4, 8):
            self.assertTrue(self.rook_white.valid_positions(3, 3, 3, i))

        self.rook_white.board.set_piece(3, 5, self.rook_white)
        for i in range(4, -1, -1):
            self.assertTrue(self.rook_white.valid_positions(3, 5, 3, i))

    def test_blocked_by_same_color(self):
        self.rook_white.board.set_piece(3, 3, self.rook_white)
        self.rook_white.board.set_piece(4, 3, Rook("white", self.board))
        for i in range(5, 8):
            self.assertFalse(self.rook_white.valid_positions(3, 3, i, 3))

        self.rook_white.board.set_piece(5, 3, self.rook_white)
        self.rook_white.board.set_piece(4, 3, Rook("white", self.board))
        for i in range(3, -1, -1):
            self.assertFalse(self.rook_white.valid_positions(5, 3, i, 3))

        self.rook_white.board.set_piece(3, 3, self.rook_white)
        self.rook_white.board.set_piece(3, 4, Rook("white", self.board))
        for i in range(5, 8):
            self.assertFalse(self.rook_white.valid_positions(3, 3, 3, i))

        self.rook_white.board.set_piece(3, 5, self.rook_white)
        self.rook_white.board.set_piece(3, 4, Rook("white", self.board))
        for i in range(3, -1, -1):
            self.assertFalse(self.rook_white.valid_positions(3, 5, 3, i))

    def test_blocked_by_opposite_color(self):
        self.rook_white.board.set_piece(3, 3, self.rook_white)
        self.rook_white.board.set_piece(4, 3, Rook("black", self.board))
        self.assertTrue(self.rook_white.valid_positions(3, 3, 4, 3))
        for i in range(5, 8):
            self.assertFalse(self.rook_white.valid_positions(3, 3, i, 3))

        self.rook_white.board.set_piece(5, 3, self.rook_white)
        self.rook_white.board.set_piece(4, 3, Rook("black", self.board))
        self.assertTrue(self.rook_white.valid_positions(5, 3, 4, 3))
        for i in range(3, -1, -1):
            self.assertFalse(self.rook_white.valid_positions(5, 3, i, 3))

        self.rook_white.board.set_piece(3, 3, self.rook_white)
        self.rook_white.board.set_piece(3, 4, Rook("black", self.board))
        self.assertTrue(self.rook_white.valid_positions(3, 3, 3, 4))
        for i in range(5, 8):
            self.assertFalse(self.rook_white.valid_positions(3, 3, 3, i))