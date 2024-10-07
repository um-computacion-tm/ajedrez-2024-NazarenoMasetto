from juego.piece import Piece
class Knight(Piece):
    def __init__(self, color):
        """
        Constructor de la clase Knight. Llama al constructor de la clase base Piece.
        :param color: El color del caballo ('White' o 'Black').
        """
        super().__init__(color)

    def valid_moves(self, current_position, board):
        """
        Calcula los movimientos válidos del caballo según las reglas del ajedrez.
        El caballo se mueve en forma de "L" (2 casillas en una dirección y 1 en otra).
        :param current_position: La posición actual del caballo en coordenadas de matriz.
        :param board: El estado actual del tablero (lista de listas).
        :return: Una lista de posiciones válidas en formato (fila, columna) para mover el caballo.
        """
        row, col = current_position
        moves = []
        
        # Definir los 8 movimientos posibles del caballo (2 en una dirección y 1 en otra)
        knight_moves = [
            (2, 1), (2, -1),  # 2 filas, 1 columna
            (-2, 1), (-2, -1),  # -2 filas, 1 columna
            (1, 2), (1, -2),  # 1 fila, 2 columnas
            (-1, 2), (-1, -2)  # -1 fila, 2 columnas
        ]

        for dr, dc in knight_moves:
            new_row, new_col = row + dr, col + dc
            # Verificar que el movimiento está dentro del tablero
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                if board[new_row][new_col] == " " or board[new_row][new_col].get_color() != self.get_color():
                    moves.append((new_row, new_col))  # Casilla vacía o captura válida

        return moves

    def get_symbol(self):
        """
        Devuelve el símbolo que representa el caballo en el tablero.
        'N' para caballo blanco y 'n' para caballo negro.
        :return: Un string con el símbolo del caballo.
        """
        return "N" if self.get_color() == 'White' else "n"



