import enum
from AI import opponent

class Board:
    def __init__(self, num_humans, first_turn, difficulty):
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
        
        self.difficulty = difficulty

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
        print("===================")
        for row in self.curr_layout:
            print ("| " + str(row[0]) + " " + str(row[1]) + " " + str(row[2]) + " " + str(row[3]) + " " + str(row[4]) + " " + str(row[5]) + " " + str(row[6]) + " " + str(row[7]) + " |")
        print("===================")

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
        
    def create_opponent(self):
        self.AI = opponent(self.difficulty)
        
    def changePiece(self, move):
        self.curr_layout[move[0]][move[1]] = self.curr_turn
        
    def generate_legal_moves(self):
        direction = 0
        player_2 = 2
        player_1 = 1
        opponent_prev = False
        if (self.curr_turn == player_1):
            opponent_piece = player_2
            player_piece = player_1
        else:
            opponent_piece = player_1
            player_piece = player_2
        for row in range(len(self.curr_layout)):
            print(row)
            for piece in range(len(self.curr_layout[row])):
                print(piece)
                if (self.curr_layout[row][piece] == player_piece):
                    print("")
                    print("")
                    columnIndex = piece
                    rowIndex = row
                    print("Checking Piece at row: " + str(rowIndex) + " Column: " + str(columnIndex))
                    self.curr_layout = self.checkDiagonals(rowIndex, columnIndex, player_piece, opponent_piece, opponent_prev, direction)
                    self.curr_layout = self.checkColumn(rowIndex, columnIndex, player_piece, opponent_piece, opponent_prev, direction)
                    self.curr_layout = self.checkRow(rowIndex, columnIndex, player_piece, opponent_piece, opponent_prev, direction)

    def checkRow(self, row, column, player, opponent, opponent_prev, direction):
        possible_move = 3
        empty_space = 0
        if (direction == 0):
            self.curr_layout = self.checkRow(row, column, player, opponent, opponent_prev, 1)
            self.curr_layout = self.checkRow(row, column, player, opponent, opponent_prev, 2)
        elif (direction == 1):
            #return if outside of board
            if (len(self.curr_layout[row]) > column > 0):
                column = column - 1
            else:
                return self.curr_layout
        elif (direction == 2):
            #return if outside of board
            if (len(self.curr_layout[row]) > column > 0):
                column = column + 1
            else:
                return self.curr_layout
        #check if these are valid moves
        print("Check Row")
        print("Row: " + str(row) + " " + "Column: " + str(column))
        print(self.curr_layout[row])
        print(self.curr_layout[row][column])
        if (self.curr_layout[row][column] == possible_move):
            return self.curr_layout
        elif (self.curr_layout[row][column] == opponent):
            opponent_prev = True
            self.curr_layout = self.checkRow(row, column, player, opponent, opponent_prev, direction)
            return self.curr_layout
        elif (self.curr_layout[row][column] == player):
            return self.curr_layout
        elif (self.curr_layout[row][column] == empty_space and opponent_prev):
            self.curr_layout[row][column] = possible_move
            self.print_layout()
            return self.curr_layout
        elif (self.curr_layout[row][column] == empty_space):
            return self.curr_layout
    
    def checkColumn(self, row, column, player, opponent, opponent_prev, direction):
        possible_move = 3
        empty_space = 0
        if (direction == 0):
            self.curr_layout = self.checkColumn(row, column, player, opponent, opponent_prev, 1)
            self.curr_layout = self.checkColumn(row, column, player, opponent, opponent_prev, 2)
        elif (direction == 1):
            #return if outside of board
            if (len(self.curr_layout) > row > 0):
                row = row - 1
            else:
                return self.curr_layout
        elif (direction == 2):
            #return if outside of board
            if (len(self.curr_layout) > row > 0):
                row = row + 1
            else:
                return self.curr_layout
        #check if these are valid moves
        print("Check Column")
        print("Row: " + str(row) + " " + "Column: " + str(column))
        print(self.curr_layout[row])
        print(self.curr_layout[row][column])
        if (self.curr_layout[row][column] == possible_move):
            return self.curr_layout
        elif (self.curr_layout[row][column] == opponent):
            opponent_prev = True
            self.curr_layout = self.checkColumn(row, column, player, opponent, opponent_prev, direction)
            return self.curr_layout
        elif (self.curr_layout[row][column] == player):
            return self.curr_layout
        elif (self.curr_layout[row][column] == empty_space and opponent_prev):
            self.curr_layout[row][column] = possible_move
            self.print_layout()
            return self.curr_layout
        elif (self.curr_layout[row][column] == empty_space):
            return self.curr_layout
        
    def checkDiagonals(self, row, column, player, opponent, opponent_prev, direction):
        possible_move = 3
        empty_space = 0
        #go left right etc
        if (direction == 0):
            self.curr_layout = self.checkDiagonals(row, column, player, opponent, opponent_prev, 1)
            self.curr_layout = self.checkDiagonals(row, column, player, opponent, opponent_prev, 2)
            self.curr_layout = self.checkDiagonals(row, column, player, opponent, opponent_prev, 3)
            self.curr_layout = self.checkDiagonals(row, column, player, opponent, opponent_prev, 4)
        elif (direction == 1):
            #return if outside of board
            if (len(self.curr_layout) > row > 0):
                row = row - 1
            else:
                return self.curr_layout
            if (len(self.curr_layout[row]) > column > 0):
                column = column - 1
            else:
                return self.curr_layout
        elif (direction == 2):
            #return if outside of board
            if (len(self.curr_layout) > row > 0):
                row = row - 1
            else:
                return self.curr_layout
            if (len(self.curr_layout[row]) > column > 0):
                column = column + 1
            else:
                return self.curr_layout
        elif (direction == 3):
            #return if outside of board
            if (len(self.curr_layout) > row > 0):
                row = row + 1
            else:
                return self.curr_layout
            if (len(self.curr_layout[row]) > column > 0):
                column = column - 1
            else:
                return self.curr_layout
        elif (direction == 4):
            #return if outside of board
            if (len(self.curr_layout) > row > 0):
                row = row + 1
            else:
                return self.curr_layout
            if (len(self.curr_layout[row]) > column > 0):
                column = column + 1
            else:
                return self.curr_layout
        #check if these are valid moves
        print("Check Diagnol")
        print("Row: " + str(row) + " " + "Column: " + str(column))
        print(self.curr_layout[row])
        print(self.curr_layout[row][column])
        if (self.curr_layout[row][column] == possible_move):
            return self.curr_layout
        elif (self.curr_layout[row][column] == opponent):
            opponent_prev = True
            self.curr_layout = self.checkDiagonals(row, column, player, opponent, opponent_prev, direction)
            return self.curr_layout
        elif (self.curr_layout[row][column] == player):
            return self.curr_layout
        elif (self.curr_layout[row][column] == empty_space and opponent_prev):
            self.curr_layout[row][column] = possible_move
            self.print_layout()
            return self.curr_layout
        elif (self.curr_layout[row][column] == empty_space):
            return self.curr_layout
        

