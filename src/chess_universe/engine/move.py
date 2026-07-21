from __future__ import annotations


class Move:
    """
    Representa un movimiento de ajedrez.
    """

    def __init__(
        self,
        start_row: int,
        start_col: int,
        end_row: int,
        end_col: int,
        piece=None,
        captured_piece=None,
    ):
        self.start_row = start_row
        self.start_col = start_col

        self.end_row = end_row
        self.end_col = end_col

        self.piece = piece
        self.captured_piece = captured_piece

        self.is_capture = captured_piece is not None

        self.is_castling = False
        self.is_en_passant = False
        self.is_promotion = False
        self.promoted_piece = None

    def __repr__(self):

        return (
            f"{self.piece}: "
            f"({self.start_row},{self.start_col})"
            f" -> "
            f"({self.end_row},{self.end_col})"
        )

    def __eq__(self, other):

        if not isinstance(other, Move):
            return False

        return (
            self.start_row == other.start_row
            and self.start_col == other.start_col
            and self.end_row == other.end_row
            and self.end_col == other.end_col
        )