import unittest
from king import King 
from queen import Queen
from bishop import Bishop
from rook import Rook
from knight import Knight
from pawn import Pawn
from board import Board



class TestBoard(unittest.TestCase):
    def test_init(self):
        board = Board()
        self.assertEqual(len(board.Boardpositions_), 8)
        self.assertEqual(len(board.Boardpositions_[0]), 8)

    def test_get_piece(self):
        board = Board()
        self.assertIsInstance(board.get_piece(0, 0), Rook)
        self.assertIsInstance(board.get_piece(0, 1), Knight)
        self.assertIsInstance(board.get_piece(0, 2), Bishop)
        self.assertIsInstance(board.get_piece(0, 3), Queen)
        self.assertIsInstance(board.get_piece(0, 4), King)
        self.assertIsInstance(board.get_piece(0, 5), Bishop)
        self.assertIsInstance(board.get_piece(0, 6), Knight)
        self.assertIsInstance(board.get_piece(0, 7), Rook)

        self.assertIsInstance(board.get_piece(7, 0), Rook)
        self.assertIsInstance(board.get_piece(7, 1), Knight)
        self.assertIsInstance(board.get_piece(7, 2), Bishop)
        self.assertIsInstance(board.get_piece(7, 3), Queen)
        self.assertIsInstance(board.get_piece(7, 4), King)
        self.assertIsInstance(board.get_piece(7, 5), Bishop)
        self.assertIsInstance(board.get_piece(7, 6), Knight)
        self.assertIsInstance(board.get_piece(7, 7), Rook)

        self.assertIsInstance(board.get_piece(1, 0), Pawn)
        self.assertIsInstance(board.get_piece(1, 1), Pawn)
        self.assertIsInstance(board.get_piece(1, 2), Pawn)
        self.assertIsInstance(board.get_piece(1, 3), Pawn)
        self.assertIsInstance(board.get_piece(1, 4), Pawn)
        self.assertIsInstance(board.get_piece(1, 5), Pawn)
        self.assertIsInstance(board.get_piece(1, 6), Pawn)
        self.assertIsInstance(board.get_piece(1, 7), Pawn)

        self.assertIsInstance(board.get_piece(6, 0), Pawn)
        self.assertIsInstance(board.get_piece(6, 1), Pawn)
        self.assertIsInstance(board.get_piece(6, 2), Pawn)
        self.assertIsInstance(board.get_piece(6, 3), Pawn)
        self.assertIsInstance(board.get_piece(6, 4), Pawn)
        self.assertIsInstance(board.get_piece(6, 5), Pawn)
        self.assertIsInstance(board.get_piece(6, 6), Pawn)
        self.assertIsInstance(board.get_piece(6, 7), Pawn)

    def test_str(self):
        board = Board()
        self.assertIsInstance(str(board), str)

if Board == '_main_':
    unittest.main()