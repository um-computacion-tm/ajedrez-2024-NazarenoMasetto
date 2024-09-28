from abc import ABC, abstractmethod

class Piece(ABC):
    def __init__(self, color):
        
        self.__color__ = color

    def get_color(self):
        
        return self.__color__

    @abstractmethod
    def valid_moves(self, current_position, board):
        
        pass

    @abstractmethod
    def get_symbol(self):
       
        pass

    def __str__(self):
        
        return self.get_symbol()

    def get_moves_in_directions(self, current_position, board, directions):
        
        row, col = current_position
        moves = []

        for dr, dc in directions:
            moves += self.__explore_direction(row, col, dr, dc, board)

        return moves

    def __explore_direction(self, row, col, dr, dc, board):
       
        new_row, new_col = row + dr, col + dc
        moves = []

        while self.__is_within_board(new_row, new_col):
            if self.__can_move_to(new_row, new_col, board):
                moves.append((new_row, new_col))
                if self.__is_capture(new_row, new_col, board):
                    break
            else:
                break

            new_row += dr
            new_col += dc

        return moves

    def __is_within_board(self, row, col):
        
        return 0 <= row < 8 and 0 <= col < 8

    def __can_move_to(self, row, col, board):
        
        return board[row][col] == " " or board[row][col].get_color() != self.get_color()

    def __is_capture(self, row, col, board):
       
        return board[row][col] != " " and board[row][col].get_color() != self.get_color()
