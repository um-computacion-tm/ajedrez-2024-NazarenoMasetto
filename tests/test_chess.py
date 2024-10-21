import unittest
from juego.chess import Chess

class TestChess(unittest.TestCase):
    def setUp(self):
        self.game = Chess()

    def test_move_valid(self):
        self.game.move(6, 4, 4, 4)  # e2 -> e4
        board = self.game.board.get_board()
        self.assertIsNone(board[6][4])  # e2 should now be empty
        self.assertIsInstance(board[4][4], Pawn)  # e4 should now have a Pawn

    def test_move_invalid_no_piece(self):
        with self.assertRaises(ValueError):
            self.game.move(4, 4, 5, 5)  # No piece at e3 (4,4)

    def test_change_turn(self):
        self.assertEqual(self.game.turn, "White")
        self.game.move(6, 4, 4, 4)  # White's move
        self.assertEqual(self.game.turn, "Black")

