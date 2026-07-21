from abc import ABC, abstractmethod


class Piece(ABC):
    """
    Clase base para todas las piezas del ajedrez.
    """

    def __init__(self, color: str, row: int, col: int):
        self.color = color
        self.row = row
        self.col = col
        self.has_moved = False

    def move_to(self, row: int, col: int):
        """Actualiza la posición de la pieza."""
        self.row = row
        self.col = col
        self.has_moved = True

    def is_enemy(self, piece) -> bool:
        """
        Devuelve True si la pieza pertenece al rival.
        """
        return piece is not None and piece.color != self.color

    def is_friend(self, piece) -> bool:
        """
        Devuelve True si la pieza pertenece al mismo jugador.
        """
        return piece is not None and piece.color == self.color

    @abstractmethod
    def get_legal_moves(self, board):
        """
        Devuelve una lista de movimientos legales.
        """
        pass

    def __repr__(self):
        return (
            f"{self.__class__.__name__}"
            f"({self.color}, ({self.row}, {self.col}))"
        )