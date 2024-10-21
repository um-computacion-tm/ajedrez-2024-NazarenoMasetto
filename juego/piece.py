class Piece:
    def __init__(self, color):
        self.__color__ = color  # Atributo privado para el color de la pieza

    def get_color(self):
        return self.__color__  # Método para obtener el color de la pieza

    def valid_moves(self, current_position, board):
        """Este método debe ser implementado por cada pieza en particular."""
        raise NotImplementedError("Este método debe ser implementado en las subclases")

    def get_symbol(self):
        """Este método debe ser implementado por cada pieza en particular."""
        raise NotImplementedError("Este método debe ser implementado en las subclases")

    def __str__(self):
        return self.get_symbol()  # Representación de la pieza como símbolo

    def calculate_valid_moves(self, current_position, possible_moves, board):
        """Calcula todos los movimientos válidos basados en las posibles posiciones y el estado del tablero."""
        valid_moves = []
        row, col = current_position

        for move in possible_moves:
            new_row, new_col = self._calculate_new_position(row, col, move)

            if self._is_within_board(new_row, new_col) and self._can_move_to(new_row, new_col, board):
                valid_moves.append((new_row, new_col))

        return valid_moves

    def _calculate_new_position(self, row, col, move):
        """Calcula las nuevas coordenadas basadas en el movimiento."""
        if isinstance(move, tuple):
            return row + move[0], col + move[1]
        return row + move["row"], col + move["col"]

    def _is_within_board(self, row, col):
        """Verifica si las coordenadas están dentro de los límites del tablero."""
        return 0 <= row < 8 and 0 <= col < 8

    def _can_move_to(self, row, col, board):
        """Verifica si la pieza puede moverse a una posición (vacía o con una pieza enemiga)."""
        target_piece = board[row][col]
        return target_piece is None or target_piece.get_color() != self.get_color()
