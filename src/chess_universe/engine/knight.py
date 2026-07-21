from chess_universe.engine.piece import Piece


class Knight(Piece):
    """Representa un caballo."""

    OFFSETS = (
        (-2, -1), (-2, 1),
        (-1, -2), (-1, 2),
        (1, -2), (1, 2),
        (2, -1), (2, 1),
    )

    def get_legal_moves(self, board):
        moves = []

        for dr, dc in self.OFFSETS:
            row = self.row + dr
            col = self.col + dc

            if not board.is_inside(row, col):
                continue

            target = board.get_piece(row, col)

            if target is None or self.is_enemy(target):
                moves.append((row, col))

        return moves