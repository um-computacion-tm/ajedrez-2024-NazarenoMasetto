from pawn import Pawn

pawn = Pawn("White")

board = [[" " for _ in range(8)] for _ in range(8)]

board[2][3] = "W"

print(pawn.valid_moves((2, 3), board))  # [(3, 3)]




pawn = Pawn("White")

board = [[" " for _ in range(8)] for _ in range(8)]

board[1][3] = "W"

print(pawn.valid_moves((1, 3), board))  # [(2, 3), (3, 3)]




pawn = Pawn("White")

board = [[" " for _ in range(8)] for _ in range(8)]

board[2][3] = "W"

board[3][2] = "B"

print(pawn.valid_moves((2, 3), board))  # [(3, 2)]



pawn = Pawn("White")

board = [[" " for _ in range(8)] for _ in range(8)]

board[2][3] = "W"

board[3][4] = "B"

print(pawn.valid_moves((2, 3), board))  # [(3, 4)]




pawn = Pawn("White")

board = [[" " for _ in range(8)] for _ in range(8)]

board[2][3] = "W"

board[3][3] = "W"

print(pawn.valid_moves((2, 3), board))  # []



pawn = Pawn("White")

board = [[" " for _ in range(8)] for _ in range(8)]

board[0][3] = "W"

print(pawn.valid_moves((0, 3), board))  # []


pawn = Pawn("White")

board = [[" " for _ in range(8)] for _ in range(8)]

board[7][3] = "W"

print(pawn.valid_moves((7, 3), board))  # []