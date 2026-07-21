from chess_universe.engine.board import Board
from chess_universe.engine.move_generator import MoveGenerator


class Game:
    """
    Controla una partida de ajedrez.

    Es el punto central del motor: administra el tablero,
    el turno, el historial de movimientos y la ejecución
    de jugadas.
    """

    WHITE = "white"
    BLACK = "black"

    def __init__(self):
        self.board = Board()
        self.board.setup()

        self.turn = self.WHITE

        self.move_history = []

        self.game_over = False
        self.winner = None

    def current_player(self):
        """Devuelve el color del jugador que debe mover."""
        return self.turn

    def switch_turn(self):
        """Cambia el turno."""
        if self.turn == self.WHITE:
            self.turn = self.BLACK
        else:
            self.turn = self.WHITE

    def get_all_moves(self):
        """
        Genera todos los movimientos pseudo-legales
        del jugador actual.
        """
        generator = MoveGenerator(self.board)
        return generator.generate_moves(self.turn)

    def make_move(self, move):
        """
        Ejecuta un movimiento sobre el tablero.
        """

        self.board.move_piece(
            move.piece,
            move.end_row,
            move.end_col
        )

        self.move_history.append(move)

        self.switch_turn()

    def move_count(self):
        """Número de movimientos realizados."""
        return len(self.move_history)

    def is_game_over(self):
        return self.game_over