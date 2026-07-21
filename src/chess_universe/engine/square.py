"""
===========================================================
Chess Universe Engine
square.py
===========================================================

Representa una casilla del tablero.
"""

from dataclasses import dataclass

from src.chess_universe.core.position import Position


@dataclass
class Square:
    """
    Una casilla del tablero.

    Attributes
    ----------
    position : Position
        Coordenadas de la casilla.

    piece : Piece | None
        Pieza colocada sobre la casilla.
    """

    position: Position
    piece: object = None

    @property
    def is_empty(self) -> bool:
        """Indica si la casilla está vacía."""
        return self.piece is None

    def __str__(self) -> str:

        if self.piece is None:
            return "."

        return str(self.piece)