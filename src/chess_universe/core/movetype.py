"""
===========================================================
Tipos de movimiento.
===========================================================
"""
from enum import Enum


class MoveType(Enum):
    NORMAL = "Normal"
    CAPTURE = "Captura"
    CASTLING = "Enroque"
    EN_PASSANT = "Captura al paso"
    PROMOTION = "Promoción"