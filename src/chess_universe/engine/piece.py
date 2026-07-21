from __future__ import annotations

from chess_universe.core.color import Color


class Piece:
    """
    Clase base para todas las piezas del ajedrez.
    """

    def __init__(self, color: Color):
        self.color = color
        self.has_moved = False

    @property
    def symbol(self) -> str:
        """
        Cada pieza devolverá su símbolo.
        """
        raise NotImplementedError

    def __repr__(self) -> str:
        return self.symbol