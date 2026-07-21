from chess_universe.engine.square import Square
from chess_universe.engine.pawn import Pawn
from chess_universe.engine.rook import Rook
from chess_universe.engine.knight import Knight
from chess_universe.engine.bishop import Bishop
from chess_universe.engine.queen import Queen
from chess_universe.engine.king import King


class Board:
    """Representa el tablero de ajedrez."""

    ROWS = 8
    COLS = 8

    def __init__(self):
        self.squares = []
        self._create_board()
        self.setup()

    def _create_board(self):
        """Crea las 64 casillas del tablero."""
        self.squares = [
            [Square(row, col) for col in range(self.COLS)]
            for row in range(self.ROWS)
        ]

    def get_square(self, row: int, col: int) -> Square:
        """Devuelve una casilla del tablero."""
        return self.squares[row][col]

    def is_inside(self, row: int, col: int) -> bool:
        """Comprueba si una posición está dentro del tablero."""
        return 0 <= row < self.ROWS and 0 <= col < self.COLS

    def get_piece(self, row: int, col: int):
        """Devuelve la pieza ubicada en una casilla."""
        return self.get_square(row, col).piece

    def place_piece(self, piece):
        """Coloca una pieza en el tablero."""
        self.get_square(piece.row, piece.col).piece = piece

    def remove_piece(self, row: int, col: int):
        """Elimina una pieza del tablero."""
        self.get_square(row, col).piece = None

    def move_piece(self, piece, new_row: int, new_col: int):
        """Mueve una pieza a una nueva posición."""
        self.remove_piece(piece.row, piece.col)
        piece.move_to(new_row, new_col)
        self.place_piece(piece)

    def setup(self):
        """Coloca todas las piezas en su posición inicial."""

        # ==========================
        # Peones
        # ==========================
        for col in range(self.COLS):
            self.place_piece(Pawn("black", 1, col))
            self.place_piece(Pawn("white", 6, col))

        # ==========================
        # Torres
        # ==========================
        self.place_piece(Rook("black", 0, 0))
        self.place_piece(Rook("black", 0, 7))
        self.place_piece(Rook("white", 7, 0))
        self.place_piece(Rook("white", 7, 7))

        # ==========================
        # Caballos
        # ==========================
        self.place_piece(Knight("black", 0, 1))
        self.place_piece(Knight("black", 0, 6))
        self.place_piece(Knight("white", 7, 1))
        self.place_piece(Knight("white", 7, 6))

        # ==========================
        # Alfiles
        # ==========================
        self.place_piece(Bishop("black", 0, 2))
        self.place_piece(Bishop("black", 0, 5))
        self.place_piece(Bishop("white", 7, 2))
        self.place_piece(Bishop("white", 7, 5))

        # ==========================
        # Damas
        # ==========================
        self.place_piece(Queen("black", 0, 3))
        self.place_piece(Queen("white", 7, 3))

        # ==========================
        # Reyes
        # ==========================
        self.place_piece(King("black", 0, 4))
        self.place_piece(King("white", 7, 4))