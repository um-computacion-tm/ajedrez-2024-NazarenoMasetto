class Piece:
    def __init__(self, color, board):
        self.__color__ = color
        self.__board__ = board

    def __str__(self):
        raise NotImplementedError("Subclasses must implement __str__")

    def get_color(self):
        return self.__color__


class King(Piece):
    def __init__(self, color, board):
        super().__init__(color, board)

    def __str__(self):
        if self.get_color() == "WHITE":
            return "White King"
        else:
            return "Black King"


class Queen(Piece):
    def __init__(self, color, board):
        super().__init__(color, board)

    def __str__(self):
        if self.get_color() == "WHITE":
            return "White Queen"
        else:
            return "Black Queen"


class Rook(Piece):
    def __init__(self, color, board):
        super().__init__(color, board)

    def __str__(self):
        if self.get_color() == "WHITE":
            return "White Rook"
        else:
            return "Black Rook"


class Bishop(Piece):
    def __init__(self, color, board):
        super().__init__(color, board)

    def __str__(self):
        if self.get_color() == "WHITE":
            return "White Bishop"
        else:
            return "Black Bishop"


class Knight(Piece):
    def __init__(self, color, board):
        super().__init__(color, board)

    def __str__(self):
        if self.get_color() == "WHITE":
            return "White Knight"
        else:
            return "Black Knight"


class Pawn(Piece):
    def __init__(self, color, board):
        super().__init__(color, board)

    def __str__(self):
        if self.get_color() == "WHITE":
            return "White Pawn"
        else:
            return "Black Pawn"