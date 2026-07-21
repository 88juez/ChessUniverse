from chess_universe.engine.board import Board


def main():
    board = Board()

    print(len(board.squares))
    print(len(board.squares[0]))

    print(board.get_square(0, 0).row, board.get_square(0, 0).col)
    print(board.get_square(7, 7).row, board.get_square(7, 7).col)


if __name__ == "__main__":
    main()