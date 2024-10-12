from juego.piece import Piece

class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)

    def valid_moves(self, current_position, board):
        
        row, col = current_position
        directions = [
            (-1, 0), (1, 0),  # Vertical
            (0, -1), (0, 1),  # Horizontal
            (-1, -1), (-1, 1),  # Diagonales
            (1, -1), (1, 1)
        ]
        valid_moves = []

        for dr, dc in directions:
            for step in range(1, 8):  # La reina puede moverse hasta 8 casillas en una dirección
                new_row, new_col = row + dr * step, col + dc * step

                # Verificar que no salga del tablero
                if not (0 <= new_row < 8 and 0 <= new_col < 8):
                    break
                
                target_square = board[new_row][new_col]
                if target_square == " ":
                    valid_moves.append((new_row, new_col))
                elif target_square.get_color() != self.get_color():
                    valid_moves.append((new_row, new_col))  # Captura válida
                    break
                else:
                    break

        return valid_moves

    def get_symbol(self):
        
        return "Q" if self.get_color() == 'White' else "q"


