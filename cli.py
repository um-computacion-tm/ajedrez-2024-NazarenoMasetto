class AjedrezCli:
    def __init__(self, board):
        self.__board__ = board
        self.__current_turn__ = "White"

    def start_game(self):
        print("¡Bienvenido al ajedrez!")
        game_over = False

        while not game_over:
            self.print_board()
            game_over = self.process_turn()

        print("El juego ha terminado.")

    def process_turn(self):
        try:
            start, end = self.get_move()
            self.__board__.move_piece(start, end)
            self.switch_turn()
        except ValueError as e:
            print(f"Error: {e}")
        except KeyboardInterrupt:
            print("\nJuego interrumpido.")
            return True

        return self.check_game_over()

    def switch_turn(self):
        self.__current_turn__ = "Black" if self.__current_turn__ == "White" else "White"

    def print_board(self):
        print("    a   b   c   d   e   f   g   h")
        print("  +---+---+---+---+---+---+---+---+")
        for i, row in enumerate(self.__board__.__board__):
            print(f"{8 - i} | " + " | ".join([str(piece) if piece != " " else " " for piece in row]) + f" | {8 - i}")
            print("  +---+---+---+---+---+---+---+---+")
        print("    a   b   c   d   e   f   g   h")

    def get_move(self):
        while True:
            move = input(f"{self.__current_turn__}, introduce tu movimiento (e.g., 'e2 e4'): ")
            parts = move.split()

            if len(parts) != 2 or not self.is_valid_position(parts[0]) or not self.is_valid_position(parts[1]):
                print("Formato inválido. Introduce un movimiento en formato 'e2 e4'.")
            else:
                return parts[0], parts[1]

    @staticmethod
    def is_valid_position(pos):
        if len(pos) != 2:
            return False
        col, row = pos[0], pos[1]
        return col in 'abcdefgh' and row in '12345678'

    def check_game_over(self):
        return False
