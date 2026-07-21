class Square:
    """Una casilla del tablero."""

    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col
        self.piece = None

    def is_empty(self) -> bool:
        return self.piece is None