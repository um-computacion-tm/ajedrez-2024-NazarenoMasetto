
from juego.piece import Piece
import unittest
# Subclase para testear Piece
class TestPiece(Piece):
    def valid_moves(self, current_position, board):
        # Para este test, solo devolveremos una lista vacía (no implementamos lógica de movimientos reales).
        return []
    def get_symbol(self):
        # Solo devolvemos un símbolo genérico para esta pieza de prueba.
        return "T"
class TestPieceClass(unittest.TestCase):
    def setUp(self):
        self.white_piece = TestPiece("White")
        self.black_piece = TestPiece("Black")
    def test_get_color(self):
        """Test para verificar que el color de la pieza se devuelve correctamente."""
        self.assertEqual(self.white_piece.get_color(), "White")
        self.assertEqual(self.black_piece.get_color(), "Black")
    def test_get_symbol(self):
        """Test para verificar que el símbolo de la pieza es devuelto correctamente."""
        self.assertEqual(str(self.white_piece), "T")  # Llama a __str__, que usa get_symbol()
        self.assertEqual(str(self.black_piece), "T")
    def test_valid_moves(self):
        """Test para verificar que valid_moves devuelve una lista (aunque vacía en esta subclase)."""
        moves = self.white_piece.valid_moves((0, 0), [])
        self.assertIsInstance(moves, list)
        self.assertEqual(len(moves), 0)  # Debe devolver una lista vacía en esta implementación de prueba
if __name__ == "__main__":
    unittest.main()