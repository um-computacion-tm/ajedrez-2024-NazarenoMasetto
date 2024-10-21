import unittest
from juego.board import Board
from juego.pawn import Pawn
from juego.king import King
from juego.rook import Rook

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()

    def test_initial_board_setup(self):
        """Verifica que el tablero se inicializa correctamente."""
        board = self.board.get_board()
        self.assertEqual(board[4][4], " ")  # Espacio vacío

    def test_move_piece_valid(self):
        """Verifica que una pieza se mueve correctamente de una posición a otra."""
        self.board.move_piece("e2", "e4")
        board = self.board.get_board()
        self.assertEqual(board[6][4], " ")  # La casilla e2 debe estar vacía (índice 6,4)
        self.assertIsInstance(board[4][4], Pawn)  # La casilla e4 debe tener un peón blanco

    def test_pawn_capture(self):
        """Verifica que un peón pueda capturar una pieza en diagonal."""
        self.board.move_piece("e2", "e4")  # Mueve el peón blanco de e2 a e4
        self.board.move_piece("d7", "d5")  # Mueve el peón negro de d7 a d5
        self.board.move_piece("e4", "d5")  # Peón blanco captura peón negro en d5
        board = self.board.get_board()
        self.assertEqual(board[4][4], " ")  # La casilla e4 debe estar vacía
        self.assertIsInstance(board[3][3], Pawn)  # La casilla d5 debe tener un peón blanco

    def test_check_king_movement(self):
        """Verifica que el rey se mueva correctamente."""
        self.board.move_piece("e1", "e2")  # Mueve el rey de e1 a e2
        board = self.board.get_board()
        self.assertIsInstance(board[1][4], King)  # Verifica que el rey se movió a la casilla e2

if __name__ == '__main__':
    unittest.main()

