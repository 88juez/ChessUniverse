"""
===========================================================
CHESS UNIVERSE
Versión 0.1.0
Sprint 1 - Parte 4
===========================================================
"""

from src.chess_universe.engine.board import Board
from src.chess_universe.engine.move import Move
from src.chess_universe.core.position import Position


def main():

    board = Board()

    print("=" * 60)
    print("POSICIÓN INICIAL")
    print("=" * 60)

    board.print_board()

    print("\nMoviendo peón e2 → e4...\n")

    move = Move(
        Position.from_algebraic("e2"),
        Position.from_algebraic("e4"),
    )

    board.move_piece(move)

    print("=" * 60)
    print("DESPUÉS DEL MOVIMIENTO")
    print("=" * 60)

    board.print_board()

    print("\nMovimiento realizado:")
    print(move)


if __name__ == "__main__":
    main()