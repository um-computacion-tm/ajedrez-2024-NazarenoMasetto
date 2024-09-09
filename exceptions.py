class InvalidMove(Exception):
    """Base exception class for invalid moves."""

    def __init__(self, message):
        super().__init__(message)

class InvalidTurn(InvalidMove):
    """Exception for attempting to move another player's piece."""

    def __init__(self):
        super().__init__("No puedes mover pieza de otro jugador")

class EmptyPosition(InvalidMove):
    """Exception for attempting to move from an empty position."""

    def __init__(self):
        super().__init__("La posicion esta vacia")

class OutOfBoard(InvalidMove):
    """Exception for attempting to move to a position outside the board."""

    def __init__(self):
        super().__init__("La posicion indicada se encuentra fuera del tablero")

class InvalidPiece(InvalidMove):
    """Exception for attempting to move a piece that is not allowed to move."""

    def __init__(self):
        super().__init__("La pieza seleccionada no se puede mover")

class BlockedPosition(InvalidMove):
    """Exception for attempting to move to a position that is blocked by another piece."""

    def __init__(self):
        super().__init__("La posicion esta bloqueada por otra pieza")

class InvalidDestination(InvalidMove):
    """Exception for attempting to move to a position that is not a valid destination."""

    def __init__(self):
        super().__init__("La posicion de destino no es valida")

class NotYourTurn(InvalidMove):
    """Exception for attempting to move when it's not your turn."""

    def __init__(self):
        super().__init__("No es tu turno")