"""
===========================================================
Chess Universe Engine
piece.py
===========================================================
"""

from abc import ABC, abstractmethod

from src.chess_universe.core.color import Color
from src.chess_universe.core.piecetype import PieceType


class Piece(ABC):
    """
    Clase base para todas las piezas.
    """

    def __init__(
        self,
        color: Color,
        piece_type: PieceType,
        symbol: str,
        value: int,
    ):

        self.color = color
        self.piece_type = piece_type
        self.symbol = symbol
        self.value = value

        self.has_moved = False

    @abstractmethod
    def legal_moves(self, board, position):
        """
        Devuelve los movimientos legales.
        """
        pass

    def __str__(self):

        return self.symbol