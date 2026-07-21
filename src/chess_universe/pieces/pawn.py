from chess_universe.engine.piece import Piece


class Pawn(Piece):

    @property
    def symbol(self) -> str:
        return "♙" if self.color.value == "white" else "♟"