import enum
from AI import opponent

class Board:
    def __init__(self, num_humans, first_turn, difficulty):
        #TODO initial attributes in constructor - difficulty, show / hide moves, number of human players

        self.num_humans = num_humans
        self.curr_turn = first_turn
        self.difficulty = difficulty

        self.player1_pieces = 2

        self.player2_pieces = 2

        self.curr_layout = [
            [3,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,1,2,0,0,0],
            [0,0,0,2,1,0,0,0],
            [0,0,0,0,3,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0]]

        self.game_over = False

    def place_piece(self, move, player):
        # If the move is valid, will add the move to the board
        y,x = move
        if (self.check_valid_move(move)):
            self.curr_layout[x][y] = player

        # Reaccumulate all pieces on the board
        self.player1_pieces = 0
        self.player2_pieces = 0
        for row in self.curr_layout:
            for number in row:
                if (number == 1):
                    self.player1_pieces += 1
                elif (number == 2):
                    self.player2_pieces += 1

    def get_turn_from_human(self):

        #TODO ----------------- PLACEHOLDER FOR TESTING -----------------
        x,y = map(int, input("---------------Player 1: row and column to play (x y)? ---------------").split())
        move = (x,y)
        return move

    def get_turn_from_ai(self, layout):

        #TODO ----------------- PLACEHOLDER FOR TESTING -----------------
        x,y = map(int, input("---------------Player 2: row and column to play (x y)? ---------------").split())
        move = (x,y)
        return move

    # Retrieves move from whoever is currently in turn, AI or human
    def get_turn_from_player(self, player_num):

        if (player_num == 1):
            return self.get_turn_from_human()

        elif (player_num == 2):
            return self.get_turn_from_ai(self.curr_layout)

    # Gets the move being played for the current turn. If a valid move, plays the move, otherwise nothing
    # GUI loop will call to swap turn if this function returns True, indicating the play was successful
    def do_move(self):
        
        move = self.get_turn_from_player(self.curr_turn)

        if(self.check_valid_move(move)):
            self.place_piece(move, self.curr_turn)
            return True # Indicates turn was successful

        else:
            False

    #def is_game_finished(self):
        #TODO check player 1 moves
        #TODO check player 2 moves

    def print_layout(self):
        print("===================")
        for row in self.curr_layout:
            print ("| " + str(row[0]) + " " + str(row[1]) + " " + str(row[2]) + " " + str(row[3]) + " " +
            str(row[4]) + " " + str(row[5]) + " " + str(row[6]) + " " + str(row[7]) + " |")
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

    def switchTurn(self):
        if (self.get_current_turn() == 1):
            self.curr_turn = 2
        else:
            self.curr_turn = 1

    def check_valid_move(self, move):
        if (self.curr_layout[move[0]][move[1]] == 3):
            return True
        else:
            return False
        
    def isPossibleMove(self):
        for rowIndex in range(len(self.curr_layout)):
            for columnIndex in range(len(self.curr_layout[rowIndex])):
                #print(self.curr_layout[rowIndex][columnIndex])
                if (self.curr_layout[rowIndex][columnIndex] == 3):
                    return True
                    #print("game still happening")
        #print("game over")
        return False

    def generate_legal_moves(self):
        possible_move = 3
        direction = 0
        player_2 = 2
        player_1 = 1
        opponent_prev = False
        #clear previous players possible moves
        for row in range(len(self.curr_layout)):
            for piece in range(len(self.curr_layout[row])):
                if (self.curr_layout[row][piece] == possible_move):
                    self.curr_layout[row][piece] = 0
        if (self.curr_turn == player_1):
            opponent_piece = player_2
            player_piece = player_1
        else:
            opponent_piece = player_1
            player_piece = player_2
        for row in range(len(self.curr_layout)):
            for piece in range(len(self.curr_layout[row])):
                if (self.curr_layout[row][piece] == player_piece):
                    columnIndex = piece
                    rowIndex = row
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
            if (len(self.curr_layout[row])-1 > column > 0):
                column = column - 1
            else:
                return self.curr_layout
        elif (direction == 2):
            #return if outside of board
            if (len(self.curr_layout[row])-1 > column > 0):
                column = column + 1
            else:
                return self.curr_layout
        #check if these are valid moves
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
            if (len(self.curr_layout)-1 > row > 0):
                row = row - 1
            else:
                return self.curr_layout
        elif (direction == 2):
            #return if outside of board
            #print(len(self.curr_layout))
            if (len(self.curr_layout)-1 > row > 0):
                row = row + 1
            else:
                return self.curr_layout
        #check if these are valid moves
        #print("Row: " + str(row))
        #print("Column: " + str(column))
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
            if (len(self.curr_layout)-1 > row > 0):
                row = row - 1
            else:
                return self.curr_layout
            if (len(self.curr_layout[row])-1 > column > 0):
                column = column - 1
            else:
                return self.curr_layout
        elif (direction == 2):
            #return if outside of board
            if (len(self.curr_layout)-1 > row > 0):
                row = row - 1
            else:
                return self.curr_layout
            if (len(self.curr_layout[row])-1 > column > 0):
                column = column + 1
            else:
                return self.curr_layout
        elif (direction == 3):
            #return if outside of board
            if (len(self.curr_layout)-1 > row > 0):
                row = row + 1
            else:
                return self.curr_layout
            if (len(self.curr_layout[row])-1 > column > 0):
                column = column - 1
            else:
                return self.curr_layout
        elif (direction == 4):
            #return if outside of board
            if (len(self.curr_layout)-1 > row > 0):
                row = row + 1
            else:
                return self.curr_layout
            if (len(self.curr_layout[row])-1 > column > 0):
                column = column + 1
            else:
                return self.curr_layout
        #check if these are valid moves
        #print("Row: " + str(row))
        #print("Column: " + str(column))
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
            return self.curr_layout
        elif (self.curr_layout[row][column] == empty_space):
            return self.curr_layout

