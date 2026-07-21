"""
===========================================================
Estado de la partida.
===========================================================
"""
from enum import Enum


class GameState(Enum):
    PLAYING = "Jugando"
    CHECK = "Jaque"
    CHECKMATE = "Jaque Mate"
    STALEMATE = "Ahogado"
    DRAW = "Tablas"