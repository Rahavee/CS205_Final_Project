import enum

class Board:
    def __init__(self, num_humans, first_turn):
        #TODO initial attributes in constructor - difficulty, show / hide moves, number of human players

        self.curr_turn = first_turn

        self.player1_pieces = 2

        self.player2_pieces = 2

        self.curr_layout = [
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,1,2,0,0,0],
            [0,0,0,2,1,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0]]

        self.game_over = False

    def place_piece(self, x, y, player): # player is a number, 1 or 2, of whose piece it will be
        # TODO check if valid move
        self.curr_layout[x][y] = player

        # Reaccumulate all pieces on the board #TODO do this while looping for valid move
        self.player1_pieces = 0
        self.player2_pieces = 0
        for row in self.curr_layout:
            for number in row:
                if (number == 1):
                    self.player1_pieces += 1
                elif (number == 2):
                    self.player2_pieces += 1
    
    def print_layout(self):
        for row in self.curr_layout:
            print (row)

    # ---------- Getters and Setters ----------

    def get_player1_pieces(self):
        return self.player1_pieces
    
    def get_player2_pieces(self):
        return self.player2_pieces

    def get_current_turn(self):
        return self.curr_turn

    def get_current_layout(self):
        return self.curr_layout
    
    #TODO unused, wrap into one function as "setters_GUI_start()"
    def set_difficulty(self, difficulty):
        self.difficulty = difficulty
    
    def set_showhide_moves(self, state):
        self.showhide_moves = state
