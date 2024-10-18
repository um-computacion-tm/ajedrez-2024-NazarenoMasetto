class Piece:
    def __init__(self, color):
        self.__color__ = color

    def get_color(self):
        return self.__color__

    def valid_moves(self, current_position, board):
        raise NotImplementedError

    def get_symbol(self):
        raise NotImplementedError

    def __str__(self):
        return self.get_symbol()
    
    def calculate_valid_moves(self, current_position, possible_moves, board):
        valid_moves = []
        row, col = current_position

        for move in possible_moves:
            new_row = row + move[0] if isinstance(move, tuple) else row + move["row"]
            new_col = col + move[1] if isinstance(move, tuple) else col + move["col"]
            
            if self._is_within_board(new_row, new_col) and self._can_move_to(new_row, new_col, board):
                valid_moves.append((new_row, new_col))
        
        return valid_moves

    def _is_within_board(self, row, col):
        return 0 <= row < 8 and 0 <= col < 8

    def _can_move_to(self, row, col, board):
        target_piece = board[row][col]
        return target_piece is None or target_piece.get_color() != self.get_color()
