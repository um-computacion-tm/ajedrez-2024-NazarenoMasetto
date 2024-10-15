from juego.piece import Piece

class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)

    def valid_moves(self, current_position, board):
        directions = self._get_directions()  # Usamos una función para obtener las direcciones
        valid_moves = []

        for direction in directions:
            self._explore_direction(current_position, direction, board, valid_moves)

        return valid_moves

    def _get_directions(self):
        # Reutilizamos esta función en otras piezas si es necesario
        return [
            (-1, 0), (1, 0),  # Vertical
            (0, -1), (0, 1),  # Horizontal
            (-1, -1), (-1, 1),  # Diagonales
            (1, -1), (1, 1)
        ]

    def _explore_direction(self, position, direction, board, valid_moves):
        for step in range(1, 8):  # La reina puede moverse hasta 8 casillas
            new_position = (position[0] + direction[0] * step, position[1] + direction[1] * step)
            if not self._is_within_board(new_position):
                break

            if self._process_square(new_position, board, valid_moves):
                break

    def _is_within_board(self, position):
        row, col = position
        return 0 <= row < 8 and 0 <= col < 8

    def _process_square(self, position, board, valid_moves):
        row, col = position
        target_square = board[row][col]
        
        if target_square == " ":
            valid_moves.append(position)
            return False  # Continúa explorando en esta dirección
        elif target_square.get_color() != self.get_color():
            valid_moves.append(position)  # Captura válida
            return True  # Detiene la exploración
        return True

    def get_symbol(self):
        return 'Q'
