"""
===========================================================
Chess Universe Engine
move.py
===========================================================

Representa un movimiento dentro de una partida.
"""

from dataclasses import dataclass

from src.chess_universe.core.position import Position
from src.chess_universe.core.movetype import MoveType


@dataclass(slots=True)
class Move:
    """
    Representa un movimiento de una pieza.
    """

    start: Position
    end: Position
    move_type: MoveType = MoveType.NORMAL

    def __str__(self) -> str:
        return (
            f"{self.start.to_algebraic()} -> "
            f"{self.end.to_algebraic()} "
            f"({self.move_type.value})"
        )