import unittest
from juego.pawn import Pawn
from juego.piece import Piece

class TestPawn(unittest.TestCase):
    
    def setUp(self):
        # Creamos un tablero vacío (8x8) para las pruebas
        self.board = [[" " for _ in range(8)] for _ in range(8)]
        self.pawn_white = Pawn("White")
        self.pawn_black = Pawn("Black")
    
    def test_pawn_single_move(self):
        # Prueba del movimiento simple hacia adelante
        self.board[6][4] = self.pawn_white  # Peón blanco en e2
        moves = self.pawn_white.valid_moves((6, 4), self.board)
        self.assertIn((5, 4), moves)  # El peón debe poder moverse a e3

        self.board[1][4] = self.pawn_black  # Peón negro en e7
        moves = self.pawn_black.valid_moves((1, 4), self.board)
        self.assertIn((2, 4), moves)  # El peón debe poder moverse a e6

    def test_pawn_double_move_first_turn(self):
        # Prueba del doble movimiento en el primer turno
        self.board[6][4] = self.pawn_white  # Peón blanco en e2
        moves = self.pawn_white.valid_moves((6, 4), self.board)
        self.assertIn((4, 4), moves)  # El peón debe poder moverse a e4

        self.board[1][4] = self.pawn_black  # Peón negro en e7
        moves = self.pawn_black.valid_moves((1, 4), self.board)
        self.assertIn((3, 4), moves)  # El peón debe poder moverse a e5

    def test_pawn_blocked_move(self):
        # Prueba de bloqueo del peón
        self.board[5][4] = Pawn("White")  # Colocar un peón blanco delante en e3
        self.board[6][4] = self.pawn_white  # Peón blanco en e2
        moves = self.pawn_white.valid_moves((6, 4), self.board)
        self.assertNotIn((5, 4), moves)  # El peón no debe poder moverse a e3

    def test_pawn_capture(self):
        # Prueba de captura diagonal
        self.board[5][3] = Pawn("Black")  # Peón negro en d3
        self.board[5][5] = Pawn("Black")  # Peón negro en f3
        self.board[6][4] = self.pawn_white  # Peón blanco en e2

        moves = self.pawn_white.valid_moves((6, 4), self.board)
        self.assertIn((5, 3), moves)  # El peón debe poder capturar en d3
        self.assertIn((5, 5), moves)  # El peón debe poder capturar en f3

    def test_pawn_no_capture_friendly(self):
        # Prueba que el peón no capture piezas amigas
        self.board[5][3] = Pawn("White")  # Peón blanco en d3
        self.board[5][5] = Pawn("White")  # Peón blanco en f3
        self.board[6][4] = self.pawn_white  # Peón blanco en e2

        moves = self.pawn_white.valid_moves((6, 4), self.board)
        self.assertNotIn((5, 3), moves)  # El peón no debe poder capturar en d3
        self.assertNotIn((5, 5), moves)  # El peón no debe poder capturar en f3

    def test_pawn_no_double_move_after_first(self):
        # Prueba que el peón no pueda moverse dos casillas después del primer turno
        self.board[5][4] = self.pawn_white  # Peón blanco en e3
        moves = self.pawn_white.valid_moves((5, 4), self.board)
        self.assertNotIn((3, 4), moves)  # El peón no debe poder moverse dos casillas

    def test_pawn_at_end_of_board(self):
        # Prueba que el peón no tenga movimientos cuando esté en la última fila
        self.board[0][4] = self.pawn_white  # Peón blanco en e8 (última fila)
        moves = self.pawn_white.valid_moves((0, 4), self.board)
        self.assertEqual(len(moves), 0)  # No debe haber movimientos

        self.board[7][4] = self.pawn_black  # Peón negro en e1 (última fila)
        moves = self.pawn_black.valid_moves((7, 4), self.board)
        self.assertEqual(len(moves), 0)  # No debe haber movimientos

if __name__ == '__main__':
    unittest.main()
