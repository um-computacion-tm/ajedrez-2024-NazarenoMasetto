from juego.piece import Piece
class Queen(Piece):
    def __init__(self, color):
        """
        Constructor de la clase Queen. Llama al constructor de la clase base Piece.
        :param color: El color de la reina ('White' o 'Black').
        """
        super().__init__(color)

    def valid_moves(self, current_position, board):
        """
        Calcula los movimientos válidos de la reina según las reglas del ajedrez.
        La reina puede moverse vertical, horizontal o diagonalmente cualquier número de casillas.
        :param current_position: La posición actual de la reina en coordenadas de matriz.
        :param board: El estado actual del tablero (lista de listas).
        :return: Una lista de posiciones válidas en formato (fila, columna) para mover la reina.
        """
        row, col = current_position
        moves = []
        
        # Definir las 8 direcciones de movimiento (vertical, horizontal y diagonal)
        directions = [
            (-1, 0), (1, 0),  # Movimientos verticales (arriba y abajo)
            (0, -1), (0, 1),  # Movimientos horizontales (izquierda y derecha)
            (-1, -1), (-1, 1),  # Movimientos diagonales (arriba-izquierda, arriba-derecha)
            (1, -1), (1, 1)    # Movimientos diagonales (abajo-izquierda, abajo-derecha)
        ]

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            # Continuar en una dirección hasta que encontremos un borde del tablero o una pieza
            while 0 <= new_row < 8 and 0 <= new_col < 8:
                if board[new_row][new_col] == " ":
                    moves.append((new_row, new_col))  # Casilla vacía, movimiento válido
                elif board[new_row][new_col].get_color() != self.get_color():
                    moves.append((new_row, new_col))  # Captura válida
                    break  # Detener después de capturar
                else:
                    break  # No puede moverse más allá de una pieza del mismo color
                new_row += dr
                new_col += dc

        return moves

    def get_symbol(self):
        """
        Devuelve el símbolo que representa la reina en el tablero.
        'Q' para reina blanca y 'q' para reina negra.
        :return: Un string con el símbolo de la reina.
        """
        return "Q" if self.get_color() == 'White' else "q"

    