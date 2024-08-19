from piece import Piece

class Pawn(Piece):
    def _init_(self, color, position=None):
        super()._init_(color, position)
        self._initial_position_ = position