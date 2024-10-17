import unittest
from juego.piece import Piece

# Subclase de prueba para la clase abstracta Piece
class TestPiece(Piece):
    def __init__(self, color):
        super().__init__(color)

    def valid_moves(self, current_position, board):
        # Implementación de prueba que retorna un movimiento válido ficticio
        return [(current_position[0] + 1, current_position[1])]

    def get_symbol(self):
        # Símbolo ficticio para la prueba
        return 'P'


class TestPieceClass(unittest.TestCase):
    def setUp(self):
        self.white_piece = TestPiece('White')
        self.black_piece = TestPiece('Black')

    def test_get_color(self):
        self.assertEqual(self.white_piece.get_color(), 'White')
        self.assertEqual(self.black_piece.get_color(), 'Black')

    def test_valid_moves(self):
        current_position = (4, 4)
        board = []  # Aquí podrías definir el estado del tablero si es necesario
        valid_moves = self.white_piece.valid_moves(current_position, board)
        expected_moves = [(5, 4)]  # Basado en la implementación ficticia
        self.assertEqual(valid_moves, expected_moves)

    def test_get_symbol(self):
        self.assertEqual(self.white_piece.get_symbol(), 'P')
        self.assertEqual(self.black_piece.get_symbol(), 'P')

    def test_str(self):
        self.assertEqual(str(self.white_piece), 'P')
        self.assertEqual(str(self.black_piece), 'P')


if __name__ == '__main__':
    unittest.main()
