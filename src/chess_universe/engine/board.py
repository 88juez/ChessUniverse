"""
===========================================================
Chess Universe Engine
board.py
===========================================================
"""
from src.chess_universe.core.color import Color

from src.chess_universe.pieces.pawn import Pawn
from src.chess_universe.pieces.rook import Rook
from src.chess_universe.pieces.knight import Knight
from src.chess_universe.pieces.bishop import Bishop
from src.chess_universe.pieces.queen import Queen
from src.chess_universe.pieces.king import King
from src.chess_universe.core.constants import BOARD_SIZE
from src.chess_universe.core.position import Position
from src.chess_universe.engine.square import Square


class Board:
    """
    Representa el tablero completo.
    """
    class Board:

        def __init__(self):

            self.squares = []

            self._create_board()
            self.setup_initial_position()

    def place_piece(self, piece, position):

        self.get_square(position).piece = piece

    def setup_initial_position(self):

        ...

    # Peones negros
        for col in range(8):
            self.place_piece(Pawn(Color.BLACK), Position(1, col))

        # Peones blancos
        for col in range(8):
            self.place_piece(Pawn(Color.WHITE), Position(6, col))

        # Torres
        self.place_piece(Rook(Color.BLACK), Position(0, 0))
        self.place_piece(Rook(Color.BLACK), Position(0, 7))
        self.place_piece(Rook(Color.WHITE), Position(7, 0))
        self.place_piece(Rook(Color.WHITE), Position(7, 7))

        # Caballos
        self.place_piece(Knight(Color.BLACK), Position(0, 1))
        self.place_piece(Knight(Color.BLACK), Position(0, 6))
        self.place_piece(Knight(Color.WHITE), Position(7, 1))
        self.place_piece(Knight(Color.WHITE), Position(7, 6))

        # Alfiles
        self.place_piece(Bishop(Color.BLACK), Position(0, 2))
        self.place_piece(Bishop(Color.BLACK), Position(0, 5))
        self.place_piece(Bishop(Color.WHITE), Position(7, 2))
        self.place_piece(Bishop(Color.WHITE), Position(7, 5))

        # Reinas
        self.place_piece(Queen(Color.BLACK), Position(0, 3))
        self.place_piece(Queen(Color.WHITE), Position(7, 3))

        # Reyes
        self.place_piece(King(Color.BLACK), Position(0, 4))
        self.place_piece(King(Color.WHITE), Position(7, 4))
        def __init__(self):

            self.squares = []

            self._create_board()

    def _create_board(self):
        """
        Crea las 64 casillas.
        """

        for row in range(BOARD_SIZE):

            board_row = []

            for col in range(BOARD_SIZE):

                board_row.append(
                    Square(Position(row, col))
                )

            self.squares.append(board_row)

    def get_square(self, position: Position) -> Square:

        return self.squares[position.row][position.col]

    def print_board(self):
        """
        Imprime el tablero.
        """

        print()

        for row in self.squares:

            print(" ".join(str(square) for square in row))

        print()

    @property
    def total_squares(self):

        return BOARD_SIZE * BOARD_SIZE