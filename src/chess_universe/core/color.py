"""
===========================================================
Chess Universe Engine
Archivo: color.py
===========================================================
"""
from enum import Enum


class Color(Enum):
    """Representa el color de una pieza."""

    WHITE = "Blanco"
    BLACK = "Negro"

    def opposite(self):
        """Devuelve el color contrario."""
        return Color.BLACK if self == Color.WHITE else Color.WHITE