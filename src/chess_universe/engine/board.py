from chess_universe.engine.square import Square


class Board:
    """Representa el tablero de ajedrez."""

    ROWS = 8
    COLS = 8

    def __init__(self):
        self.squares = []
        self._create_board()

    def _create_board(self):
        """Crea las 64 casillas."""
        self.squares = [
            [Square(row, col) for col in range(self.COLS)]
            for row in range(self.ROWS)
        ]

    def get_square(self, row: int, col: int) -> Square:
        return self.squares[row][col]