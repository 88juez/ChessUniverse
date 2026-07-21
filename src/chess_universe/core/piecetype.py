"""
===========================================================
Chess Universe Engine
Archivo: piecetype.py
===========================================================
"""
from enum import Enum


class PieceType(Enum):
    PAWN = "Peón"
    KNIGHT = "Caballo"
    BISHOP = "Alfil"
    ROOK = "Torre"
    QUEEN = "Reina"
    KING = "Rey"