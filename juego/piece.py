class Piece:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def valid_moves(self, current_position, board):
        raise NotImplementedError("Must implement valid_moves in subclasses.")

    def get_symbol(self):
        raise NotImplementedError("Must implement get_symbol in subclasses.")

    def __str__(self):
        return self.get_symbol()

    def _get_valid_moves(self, pos, moves, board, limit=1):
        """Explora las posiciones válidas en varias direcciones."""
        valid_moves = []
        for direction in moves:
            valid_moves.extend(self._explore_moves_in_direction(pos, direction, board, limit))
        return valid_moves

    def _explore_moves_in_direction(self, pos, direction, board, limit=1):
        """Explora las posiciones en una dirección específica."""
        return self._explore_in_steps(pos, direction, board, limit)

    def _explore_in_steps(self, pos, direction, board, limit):
        """Explora las posiciones paso a paso en una dirección."""
        valid_moves = []
        for step in range(1, limit + 1):
            new_row = pos[0] + direction[0] * step
            new_col = pos[1] + direction[1] * step
            if not self._is_within_board(new_row, new_col):
                break  # Detiene si se sale del tablero
            
            target_square = board[new_row][new_col]
            if target_square == " " or target_square.get_color() != self.get_color():
                valid_moves.append((new_row, new_col))  # Movimiento válido o captura
                if target_square != " ":  # Detiene si hay una pieza
                    break
        return valid_moves

    def _is_within_board(self, row, col):
        """Comprueba si una posición está dentro del tablero."""
        return 0 <= row < 8 and 0 <= col < 8

    @staticmethod
    def get_moves(move_type):
        """Retorna los movimientos dependiendo del tipo de pieza."""
        if move_type == 'knight':
            return [
                (2, 1), (2, -1), (-2, 1), (-2, -1),
                (1, 2), (1, -2), (-1, 2), (-1, -2)
            ]
        elif move_type == 'directions':
            return [
                (-1, 0), (1, 0),  # Vertical
                (0, -1), (0, 1),  # Horizontal
                (-1, -1), (-1, 1), (1, -1), (1, 1)  # Diagonal
            ]
        else:
            raise ValueError("Invalid move type provided")

