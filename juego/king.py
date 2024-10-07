from juego.piece import Piece
class King(Piece):
    def __init__(self, color):
        """
        Constructor de la clase King. Llama al constructor de la clase base Piece.
        :param color: El color del rey ('White' o 'Black').
        """
        super().__init__(color)

    def valid_moves(self, current_position, board):
        """
        Calcula los movimientos válidos del rey según las reglas del ajedrez.
        El rey puede moverse una casilla en cualquier dirección.
        :param current_position: La posición actual del rey en coordenadas de matriz.
        :param board: El estado actual del tablero (lista de listas).
        :return: Una lista de posiciones válidas en formato (fila, columna) para mover el rey.
        """
        row, col = current_position
        moves = []
        
        # Posibles direcciones de movimiento: 8 direcciones (vertical, horizontal y diagonal)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < 8 and 0 <= new_col < 8:  # Verificar que no salga del tablero
                if board[new_row][new_col] == " " or board[new_row][new_col].get_color() != self.get_color():
                    moves.append((new_row, new_col))

        return moves

    def get_symbol(self):
        """
        Devuelve el símbolo que representa el rey en el tablero.
        'K' para rey blanco y 'k' para rey negro.
        :return: Un string con el símbolo del rey.
        """
        return "K" if self.get_color() == 'White' else "k"



