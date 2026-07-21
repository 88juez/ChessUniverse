from chess_universe.engine.board import Board
from chess_universe.engine.move_generator import MoveGenerator

board = Board()
board.setup()

generator = MoveGenerator(board)

moves = generator.generate_moves("white")

print(f"Movimientos blancos: {len(moves)}")
print()

for move in moves:
    print(move)