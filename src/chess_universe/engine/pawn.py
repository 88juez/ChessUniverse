from chess_universe.engine.piece import Piece


class Pawn(Piece):
    """Representa un peón."""

    def get_legal_moves(self, board):
        moves = []

        # Dirección del movimiento
        direction = -1 if self.color == "white" else 1

        # Fila inicial
        start_row = 6 if self.color == "white" else 1

        # ===== Avance de una casilla =====
        next_row = self.row + direction

        if board.is_inside(next_row, self.col):
            if board.get_piece(next_row, self.col) is None:
                moves.append((next_row, self.col))

                # ===== Avance doble =====
                next2_row = self.row + (2 * direction)

                if (
                    self.row == start_row
                    and board.is_inside(next2_row, self.col)
                    and board.get_piece(next2_row, self.col) is None
                ):
                    moves.append((next2_row, self.col))

        # ===== Capturas diagonales =====

        for dc in (-1, 1):

            new_col = self.col + dc
            new_row = self.row + direction

            if board.is_inside(new_row, new_col):

                target = board.get_piece(new_row, new_col)

                if self.is_enemy(target):
                    moves.append((new_row, new_col))

        return moves