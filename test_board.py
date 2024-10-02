import unittest
from board import Board
from pawn import Pawn
from rook import Rook
from knight import Knight
from bishop import Bishop
from queen import Queen
from king import King

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()

    def test_initialization(self):
        """ Testea la correcta inicialización del tablero con las piezas en su posición inicial """
        initial_board = self.board._Board__board__  # Acceso a la variable privada __board__
        # Comprobar las piezas en la primera fila blanca
        self.assertIsInstance(initial_board[0][0], Rook)
        self.assertIsInstance(initial_board[0][1], Knight)
        self.assertIsInstance(initial_board[0][2], Bishop)
        self.assertIsInstance(initial_board[0][3], Queen)
        self.assertIsInstance(initial_board[0][4], King)
        self.assertIsInstance(initial_board[0][5], Bishop)
        self.assertIsInstance(initial_board[0][6], Knight)
        self.assertIsInstance(initial_board[0][7], Rook)
        
        "Comprobar los peones blancos"
        for col in range(8):
            self.assertIsInstance(initial_board[1][col], Pawn)
        
        "Comprobar que la fila de peones negros es correcta"
        for col in range(8):
            self.assertIsInstance(initial_board[6][col], Pawn)

        "Comprobar las piezas en la fila de piezas principales negras"
        self.assertIsInstance(initial_board[7][0], Rook)
        self.assertIsInstance(initial_board[7][1], Knight)
        self.assertIsInstance(initial_board[7][2], Bishop)
        self.assertIsInstance(initial_board[7][3], Queen)
        self.assertIsInstance(initial_board[7][4], King)
        self.assertIsInstance(initial_board[7][5], Bishop)
        self.assertIsInstance(initial_board[7][6], Knight)
        self.assertIsInstance(initial_board[7][7], Rook)

    def test_position_to_indices(self):
        """ Testea la conversión de la notación algebraica a índices de matriz """
        self.assertEqual(self.board.position_to_indices("a1"), (7, 0))
        self.assertEqual(self.board.position_to_indices("h8"), (0, 7))
        self.assertEqual(self.board.position_to_indices("e2"), (6, 4))

    def test_get_piece_at(self):
        """ Testea la función get_piece_at para posiciones con y sin piezas """
        self.assertIsInstance(self.board.get_piece_at((1, 0)), Pawn)  # Peón blanco en a2
        self.assertIsInstance(self.board.get_piece_at((7, 4)), King)  # Rey negro en e8
        self.assertIsNone(self.board.get_piece_at((4, 4)))  # Casilla vacía

    def test_move_piece(self):
        """ Testea el movimiento de una pieza válida """
        self.board.move_piece("e2", "e4")  # Mover un peón
        self.assertIsInstance(self.board.get_piece_at((4, 4)), Pawn)  # El peón se ha movido
        self.assertIsNone(self.board.get_piece_at((6, 4)))  # La casilla inicial ahora está vacía

    def test_invalid_move(self):
        """ Testea un movimiento inválido """
        with self.assertRaises(ValueError):
            self.board.move_piece("e2", "e5")  # Movimiento no permitido para un peón

    def test_move_empty_square(self):
        """ Testea el intento de mover una pieza desde una casilla vacía """
        with self.assertRaises(ValueError):
            self.board.move_piece("e3", "e4")  # No hay pieza en e3

    def test_capture_opponent_piece(self):
        """ Testea la captura de una pieza oponente """
        self.board.move_piece("e2", "e4")  # Mover peón blanco
        self.board.move_piece("e7", "e5")  # Mover peón negro
        self.board.move_piece("d1", "h5")  # Mover reina blanca para preparar una captura
        self.board.move_piece("h5", "e5")  # Captura de peón negro
        self.assertIsInstance(self.board.get_piece_at((4, 4)), Queen)  # La reina blanca está en e5
        self.assertIsNone(self.board.get_piece_at((6, 4)))  # El peón negro ha sido capturado

if __name__ == '__main__':
    unittest.main()
