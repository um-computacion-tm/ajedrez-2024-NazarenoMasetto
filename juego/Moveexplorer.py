class MoveExplorer:
    def __init__(self, piece, board):
        self.piece = piece
        self.board = board

    def explore(self, start_row, start_col, directions, limit=1):
        """Explora posiciones en múltiples direcciones hasta un límite."""
        valid_moves = []
        for dr, dc in directions:
            valid_moves.extend(self._explore_direction(start_row, start_col, dr, dc, limit))
        return valid_moves

    def _explore_direction(self, row, col, dr, dc, limit):
        """Explora en una dirección específica."""
        valid_moves = []
        for step in range(1, limit + 1):
            new_row, new_col = self._calculate_new_position(row, col, dr, dc, step)
            if not self._is_within_board(new_row, new_col):
                break
            if not self._process_move(new_row, new_col, valid_moves):
                break
        return valid_moves

    def _calculate_new_position(self, row, col, dr, dc, step):
        return row + dr * step, col + dc * step

    def _process_move(self, new_row, new_col, valid_moves):
        target_moves = self._evaluate_target(new_row, new_col)
        valid_moves.extend(target_moves)
        return bool(target_moves and self.board[new_row][new_col] == " ")

    def _evaluate_target(self, new_row, new_col):
        target_square = self.board[new_row][new_col]
        if target_square == " ":
            return [(new_row, new_col)]  # Movimiento vacío
        elif target_square.get_color() != self.piece.get_color():
            return [(new_row, new_col)]  # Captura
        return []  # No se puede mover

    @staticmethod
    def _is_within_board(row, col):
        return 0 <= row < 8 and 0 <= col < 8
