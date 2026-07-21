from src.chess_universe.engine.piece import Piece
from src.chess_universe.core.color import Color
from src.chess_universe.core.piecetype import PieceType


class Bishop(Piece):

    def __init__(self, color: Color):

        symbol = "♗" if color == Color.WHITE else "♝"

        super().__init__(
            color=color,
            piece_type=PieceType.BISHOP,
            symbol=symbol,
            value=3
        )

    def legal_moves(self, board, position):
        return []