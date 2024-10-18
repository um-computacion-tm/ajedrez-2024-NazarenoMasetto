from juego.piece import Piece

class Knight(Piece):
    
    def valid_positions(self, from_row, from_col, to_row, to_col):
        
        directions = self.generate_knight_directions()  
        possible_positions = self.possible_moves_general(from_row, from_col, directions, single_step=True)
        return (to_row, to_col) in possible_positions

    def generate_knight_directions(self):
       
        moves = [2, 1, -1, -2]
        return [(i, j) for i in moves for j in moves if abs(i) != abs(j)]
    
    def get_symbol(self):
        return "K" if self.get_color() == 'White' else "k"