import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from juego.rook import Rook
from juego.board import Board

class TestRook(unittest.TestCase):

    def setUp(self):
        # Crea un tablero vacío para cada prueba
        self.board = Board()

    def test_rook_initial_position(self):
        # Crea una torre blanca en la posición inicial
        rook = Rook('White')
        self.board.place_piece(rook, (0, 0))  # Coloca la torre en la esquina superior izquierda

        expected_moves = [(1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),  # Movimientos hacia abajo
                          (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7)]  # Movimientos hacia la derecha
        self.assertEqual(sorted(rook.valid_moves((0, 0), self.board)), sorted(expected_moves))

    def test_rook_blocked_by_same_color(self):
        # Crea una torre blanca y un peón blanco que bloquea
        rook = Rook('White')
        self.board.place_piece(rook, (3, 3))  # Torre en el centro
        self.board.place_piece(Rook('White'), (3, 5))  # Coloca otra pieza en la misma fila

        expected_moves = [(2, 3), (1, 3), (0, 3),  # Movimientos hacia arriba
                          (4, 3), (5, 3), (6, 3), (7, 3),  # Movimientos hacia abajo
                          (3, 2), (3, 1), (3, 0),  # Movimientos hacia la izquierda
                          (3, 4)]  # Movimiento hacia la derecha, hasta el peón
        self.assertEqual(sorted(rook.valid_moves((3, 3), self.board)), sorted(expected_moves))

    def test_rook_blocked_by_opponent(self):
        # Crea una torre blanca y una pieza enemiga que bloquea
        rook = Rook('White')
        self.board.place_piece(rook, (4, 4))  # Torre en el centro
        self.board.place_piece(Rook('Black'), (4, 6))  # Coloca una pieza enemiga en la misma fila

        expected_moves = [(3, 4), (2, 4), (1, 4), (0, 4),  # Movimientos hacia arriba
                          (5, 4), (6, 4), (7, 4),  # Movimientos hacia abajo
                          (4, 3), (4, 2), (4, 1), (4, 0),  # Movimientos hacia la izquierda
                          (4, 5), (4, 6)]  # Puede capturar la pieza enemiga
        self.assertEqual(sorted(rook.valid_moves((4, 4), self.board)), sorted(expected_moves))

    def test_rook_edge_of_board(self):
        # Crea una torre en el borde del tablero
        rook = Rook('White')
        self.board.place_piece(rook, (7, 7))  # Coloca la torre en la esquina inferior derecha

        expected_moves = [(6, 7), (5, 7), (4, 7), (3, 7), (2, 7), (1, 7), (0, 7),  # Movimientos hacia arriba
                          (7, 6), (7, 5), (7, 4), (7, 3), (7, 2), (7, 1), (7, 0)]  # Movimientos hacia la izquierda
        self.assertEqual(sorted(rook.valid_moves((7, 7), self.board)), sorted(expected_moves))

if __name__ == '__main__':
    unittest.main()
