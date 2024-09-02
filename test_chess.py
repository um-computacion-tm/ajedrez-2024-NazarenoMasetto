import unittest
from chess import Chess  
from board import Board

class TestChess(unittest.TestCase):
    def setUp(self):
        self.chess = Chess()  

    def test_init(self):
        self.assertEqual(self.chess.turn, "WHITE")  
        self.assertIsInstance(self.chess.board, Board)  

    def test_move_valid(self):
        
        self.chess.move(0, 0, 1, 1)
        self.assertEqual(self.chess.turn, "BLACK")  
    def test_move_invalid_coords(self):
        with self.assertRaises(ValueError):
            self.chess.move(-1, 0, 1, 1)  
    def test_move_no_piece(self):
        with self.assertRaises(ValueError):
            self.chess.move(0, 0, 1, 1)  
    def test_move_wrong_color(self):
        with self.assertRaises(ValueError):
            self.chess.move(0, 0, 1, 1)  
        with self.assertRaises(ValueError):
            self.chess.move(0, 0, 2, 2)  

    def test_turn(self):
        self.assertEqual(self.chess.turn, "WHITE")  
        self.chess.move(0, 0, 1, 1)  
        self.assertEqual(self.chess.turn, "BLACK")  

    def test_show_board(self):
        self.assertIsInstance(self.chess.show_board(), str)  


if Chess == "_main_":
    unittest.main()