from juego.piece import Piece

class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)

    def valid_moves(self, current_position, board):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Arriba, abajo, izquierda, derecha
        return self._generate_linear_moves(current_position, board, directions)

    def _generate_linear_moves(self, current_position, board, directions):
        moves = []
        for direction in directions:
            moves.extend(self._explore_direction(current_position[0], current_position[1], direction, board))
        return moves

    def _explore_direction(self, row, col, direction, board):
        moves = []
        new_row, new_col = row + direction[0], col + direction[1]

        while self._is_within_board(new_row, new_col):
            target_piece = board[new_row][new_col]
            if target_piece == " ":
                moves.append((new_row, new_col))
            elif target_piece.get_color() != self.get_color():
                moves.append((new_row, new_col))  # Puede capturar al oponente
                break
            else:
                break  # Bloqueado por una pieza del mismo color

            new_row += direction[0]
            new_col += direction[1]

        return moves
