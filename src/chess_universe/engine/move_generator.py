from chess_universe.engine.move import Move


class MoveGenerator:
    """
    Genera todos los movimientos legales (por ahora pseudo-legales)
    para un color determinado.
    """

    def __init__(self, board):
        self.board = board

    def generate_moves(self, color: str):
        """
        Devuelve una lista de objetos Move para todas las piezas
        del color indicado.
        """
        moves = []

        for row in range(self.board.ROWS):
            for col in range(self.board.COLS):

                piece = self.board.get_piece(row, col)

                if piece is None:
                    continue

                if piece.color != color:
                    continue

                legal_moves = piece.get_legal_moves(self.board)

                for new_row, new_col in legal_moves:

                    captured = self.board.get_piece(new_row, new_col)

                    moves.append(
                        Move(
                            start_row=row,
                            start_col=col,
                            end_row=new_row,
                            end_col=new_col,
                            piece=piece,
                            captured_piece=captured,
                        )
                    )

        return moves