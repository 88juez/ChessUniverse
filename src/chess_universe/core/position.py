"""
===========================================================
Representa una posición dentro del tablero.
===========================================================
"""
from dataclasses import dataclass
from .constants import BOARD_SIZE


@dataclass(frozen=True)
class Position:
    """
    Representa una casilla del tablero.

    row: 0-7
    col: 0-7
    """

    row: int
    col: int

    def is_valid(self) -> bool:
        """Comprueba si la posición pertenece al tablero."""
        return 0 <= self.row < BOARD_SIZE and 0 <= self.col < BOARD_SIZE

    def to_algebraic(self) -> str:
        """Convierte (6,4) -> e2"""
        file = chr(ord("a") + self.col)
        rank = str(8 - self.row)

        return f"{file}{rank}"

    @classmethod
    def from_algebraic(cls, square: str):
        file = ord(square[0].lower()) - ord("a")
        rank = 8 - int(square[1])

        return cls(rank, file)