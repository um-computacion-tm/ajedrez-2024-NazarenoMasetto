import unittest
from juego.rook import Rook
from juego.board import Board

class TestRook(unittest.TestCase):

    def setUp(self):
        self.board = Board()

    def place_piece_manually(self, piece, position):
        board = self.board.get_board()
        board[position[0]][position[1]] = piece

    def test_rook_initial_position(self):
        """Verifica los movimientos válidos de la torre desde su posición inicial."""
        rook = Rook("White")
        self.place_piece_manually(rook, (0, 0))  # Coloca la torre en la esquina superior izquierda
        expected_moves = [(i, 0) for i in range(1, 8)] + [(0, j) for j in range(1, 8)]  # Movimientos válidos
        self.assertEqual(sorted(rook.valid_moves((0, 0), self.board.get_board())), sorted(expected_moves))

    def test_rook_blocked_by_same_color(self):
        """Verifica que la torre no pueda moverse a través de piezas del mismo color."""
        rook = Rook("White")
        self.place_piece_manually(rook, (3, 3))  # Torre en el centro
        self.place_piece_manually(Rook("White"), (3, 5))  # Otra torre blanca en su camino
        expected_moves = [(i, 3) for i in range(0, 3)] + [(i, 3) for i in range(4, 8)] + [(3, j) for j in range(0, 5)]
        self.assertEqual(sorted(rook.valid_moves((3, 3), self.board.get_board())), sorted(expected_moves))

    def test_rook_blocked_by_opponent(self):
        """Verifica que la torre pueda capturar piezas del color contrario pero no moverse más allá."""
        rook = Rook("White")
        self.place_piece_manually(rook, (4, 4))  # Torre en el centro
        self.place_piece_manually(Rook("Black"), (4, 6))  # Torre negra en su camino
        expected_moves = [(i, 4) for i in range(0, 4)] + [(i, 4) for i in range(5, 8)] + [(4, j) for j in range(0, 7)]
        self.assertEqual(sorted(rook.valid_moves((4, 4), self.board.get_board())), sorted(expected_moves))

if __name__ == '__main__':
    unittest.main()
