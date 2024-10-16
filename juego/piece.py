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
            new_pos = (pos[0] + direction[0] * step, pos[1] + direction[1] * step)
            if self._is_within_board(new_pos):
                target_moves = self._evaluate_target(new_pos, board)
                valid_moves.extend(target_moves)
                if target_moves and board[new_pos[0]][new_pos[1]] != " ":
                    break  # Detiene la exploración si hay una pieza
            else:
                break  # Detiene si se sale del tablero
        return valid_moves

    def _evaluate_target(self, pos, board):
        """Evalúa el destino del movimiento."""
        target_square = board[pos[0]][pos[1]]
        if target_square == " ":
            return [pos]  # Movimiento vacío
        elif target_square.get_color() != self.get_color():
            return [pos]  # Captura
        return []  # No se puede mover

    def _is_within_board(self, pos):
        """Comprueba si una posición está dentro del tablero."""
        return 0 <= pos[0] < 8 and 0 <= pos[1] < 8

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
