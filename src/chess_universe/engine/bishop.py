from chess_universe.engine.piece import Piece


class Bishop(Piece):
    """Representa un alfil."""

    DIRECTIONS = (
        (-1, -1),
        (-1, 1),
        (1, -1),
        (1, 1),
    )

    def get_legal_moves(self, board):
        moves = []

        for dr, dc in self.DIRECTIONS:

            row = self.row + dr
            col = self.col + dc

            while board.is_inside(row, col):

                target = board.get_piece(row, col)

                # Casilla vacía
                if target is None:
                    moves.append((row, col))

                # Pieza enemiga
                elif self.is_enemy(target):
                    moves.append((row, col))
                    break

                # Pieza aliada
                else:
                    break

                row += dr
                col += dc

        return moves