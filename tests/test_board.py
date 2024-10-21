import unittest
from juego.board import Board
from juego.pawn import Pawn

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()

    def test_initial_board_setup(self):
        """Verifica que el tablero se inicializa correctamente."""
        board = self.board.get_board()
        self.assertEqual(len(board), 8)
        self.assertEqual(len(board[0]), 8)

    def test_move_piece_valid(self):
        """Verifica que una pieza se mueve correctamente de una posición a otra."""
        pawn = Pawn('White')
        self.board.place_piece(pawn, (6, 4))  # Peón blanco en e2
        self.board.move_piece('e2', 'e4')  # Mueve a e4
        board = self.board.get_board()
        self.assertIsNone(board[6][4])  # e2 debería estar vacía
        self.assertEqual(board[4][4], pawn)  # e4 debería tener el peón

    def test_pawn_capture(self):
        """Verifica que un peón puede capturar una pieza en diagonal."""
        pawn_white = Pawn('White')
        pawn_black = Pawn('Black')
        self.board.place_piece(pawn_white, (6, 4))  # Peón blanco en e2
        self.board.place_piece(pawn_black, (5, 5))  # Peón negro en f3
        self.board.move_piece('e2', 'f3')  # Captura en diagonal
        board = self.board.get_board()
        self.assertIsNone(board[6][4])  # e2 debería estar vacía
        self.assertEqual(board[5][5], pawn_white)  # f3 debería tener el peón blanco

if __name__ == '__main__':
    unittest.main()
