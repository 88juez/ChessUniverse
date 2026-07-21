from chess_universe.core.color import Color
from chess_universe.pieces.pawn import Pawn


def main():
    white = Pawn(Color.WHITE)
    black = Pawn(Color.BLACK)

    print(white)
    print(black)

    print(white.has_moved)
    print(black.has_moved)


if __name__ == "__main__":
    main()