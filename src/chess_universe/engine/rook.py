from chess_universe.engine.piece import Piece


class Rook(Piece):
    """Representa una torre."""

    DIRECTIONS = (
        (-1, 0),  # Arriba
        (1, 0),   # Abajo
        (0, -1),  # Izquierda
        (0, 1),   # Derecha
    )

    def get_legal_moves(self, board):
        moves = []

        for dr, dc in self.DIRECTIONS:

            row = self.row + dr
            col = self.col + dc

            while board.is_inside(row, col):

                target = board.get_piece(row, col)

                if target is None:
                    moves.append((row, col))

                elif self.is_enemy(target):
                    moves.append((row, col))
                    break

                else:
                    break

                row += dr
                col += dc

        return moves