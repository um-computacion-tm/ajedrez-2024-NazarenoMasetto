class Pawn:
    def valid_moves(self, position, board):
        row, col = position
        direction = 1 if self._color_ == "White" else -1
        moves = []

        """Avanza un lugar"""
        if 0 <= row + direction < 8 and board[row + direction][col] == " ":
            moves.append((row + direction, col))

        """Avanza dos casillas si es el primer movimiento del peón"""
        if (self._color_ == "White" and row == 1) or (self._color_ == "Black" and row == 6):
            if board[row + direction][col] == " " and board[row + 2 * direction][col] == " ":
                moves.append((row + 2 * direction, col))

        
        for capture_col in [col - 1, col + 1]:
            if 0 <= capture_col < 8 and 0 <= row + direction < 8:
                target_piece = board[row + direction][capture_col]
                if target_piece != " " and target_piece._color_ != self._color_:
                    moves.append((row + direction, capture_col))

        return moves