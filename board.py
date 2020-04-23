import enum
from AI import opponent


class Board:
    def __init__(self, num_humans, first_turn, difficulty):
        # TODO initial attributes in constructor - difficulty, show / hide moves, number of human players

        self.num_humans = num_humans
        self.curr_turn = first_turn
        self.difficulty = difficulty

        self.player1_pieces = 2

        self.player2_pieces = 2

        self.curr_layout = [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 2, 0, 0, 0],
            [0, 0, 0, 2, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]]

        self.game_over = False

    def reset(self):
        self.curr_layout = [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 2, 0, 0, 0],
            [0, 0, 0, 2, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]]

    def place_piece(self, move, player):
        # If the move is valid, will add the move to the board
        flag = False
        if (move == None):
            flag = True
            return flag
        x, y = move
        if (self.check_valid_move(move)):
            self.curr_layout[x][y] = player
            flag = True
            # Reaccumulate all pieces on the board
            self.player1_pieces = 0
            self.player2_pieces = 0
            for row in self.curr_layout:
                for number in row:
                    if (number == 1):
                        self.player1_pieces += 1
                    elif (number == 2):
                        self.player2_pieces += 1
        return flag

    def print_layout(self):
        print("===================")
        for row in self.curr_layout:
            print("| " + str(row[0]) + " " + str(row[1]) + " " + str(row[2]) + " " + str(row[3]) + " " +
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
                if (self.curr_layout[rowIndex][columnIndex] == 3):
                    return True
                    # print("game still happening")
        # print("game over")
        return False

    def numberOfTiles(self, player):
        total = 0
        for row in range(len(self.curr_layout)):
            for piece in range(len(self.curr_layout[row])):
                if self.curr_layout[row][piece] == player:
                    total += 1

        return total

    def determineWinner(self):
        winner = 0
        num_one = self.numberOfTiles(1)
        num_two = self.numberOfTiles(2)

        if num_one > num_two:
            winner = 1
        elif num_one < num_two:
            winner = 2
        else:
            winner = 3
        return winner

    def generate_legal_moves(self):
        possible_move = 3
        direction = 0
        player_2 = 2
        player_1 = 1
        opponent_prev = False
        # clear previous players possible moves
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
                    self.curr_layout = self.checkDiagonals(rowIndex, columnIndex, player_piece, opponent_piece,
                                                           opponent_prev, direction)
                    self.curr_layout = self.checkColumn(rowIndex, columnIndex, player_piece, opponent_piece,
                                                        opponent_prev, direction)
                    self.curr_layout = self.checkRow(rowIndex, columnIndex, player_piece, opponent_piece, opponent_prev,
                                                     direction)

    def checkRow(self, row, column, player, opponent, opponent_prev, direction):
        possible_move = 3
        empty_space = 0
        if (direction == 0):
            self.curr_layout = self.checkRow(row, column, player, opponent, opponent_prev, 1)
            self.curr_layout = self.checkRow(row, column, player, opponent, opponent_prev, 2)
        elif (direction == 1):
            # return if outside of board
            if (len(self.curr_layout[row]) - 1 > column > 0):
                column = column - 1
            else:
                return self.curr_layout
        elif (direction == 2):
            # return if outside of board
            if (len(self.curr_layout[row]) - 1 > column > 0):
                column = column + 1
            else:
                return self.curr_layout
        # check if these are valid moves
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
            # return if outside of board
            if (len(self.curr_layout) - 1 > row > 0):
                row = row - 1
            else:
                return self.curr_layout
        elif (direction == 2):
            # return if outside of board
            # print(len(self.curr_layout))
            if (len(self.curr_layout) - 1 > row > 0):
                row = row + 1
            else:
                return self.curr_layout
        # check if these are valid moves
        # print("Row: " + str(row))
        # print("Column: " + str(column))
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
        # go left right etc
        if (direction == 0):
            self.curr_layout = self.checkDiagonals(row, column, player, opponent, opponent_prev, 1)
            self.curr_layout = self.checkDiagonals(row, column, player, opponent, opponent_prev, 2)
            self.curr_layout = self.checkDiagonals(row, column, player, opponent, opponent_prev, 3)
            self.curr_layout = self.checkDiagonals(row, column, player, opponent, opponent_prev, 4)
        elif (direction == 1):
            # return if outside of board
            if (len(self.curr_layout) - 1 > row > 0):
                row = row - 1
            else:
                return self.curr_layout
            if (len(self.curr_layout[row]) - 1 > column > 0):
                column = column - 1
            else:
                return self.curr_layout
        elif (direction == 2):
            # return if outside of board
            if (len(self.curr_layout) - 1 > row > 0):
                row = row - 1
            else:
                return self.curr_layout
            if (len(self.curr_layout[row]) - 1 > column > 0):
                column = column + 1
            else:
                return self.curr_layout
        elif (direction == 3):
            # return if outside of board
            if (len(self.curr_layout) - 1 > row > 0):
                row = row + 1
            else:
                return self.curr_layout
            if (len(self.curr_layout[row]) - 1 > column > 0):
                column = column - 1
            else:
                return self.curr_layout
        elif (direction == 4):
            # return if outside of board
            if (len(self.curr_layout) - 1 > row > 0):
                row = row + 1
            else:
                return self.curr_layout
            if (len(self.curr_layout[row]) - 1 > column > 0):
                column = column + 1
            else:
                return self.curr_layout
        # check if these are valid moves
        # print("Row: " + str(row))
        # print("Column: " + str(column))
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

    def flip_pieces(self, move):
        rowIndex, columnIndex = move
        possible_move = 3
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

        self.curr_layout, valid_flip = self.flipDiagonals(rowIndex, columnIndex, player_piece, opponent_piece,
                                                          opponent_prev, direction)
        # print("Valid flip Diagnal: " + str(valid_flip))
        self.curr_layout, valid_flip = self.flipColumn(rowIndex, columnIndex, player_piece, opponent_piece,
                                                       opponent_prev, direction)
        # print("Valid flip Column: " + str(valid_flip))
        self.curr_layout, valid_flip = self.flipRow(rowIndex, columnIndex, player_piece, opponent_piece, opponent_prev,
                                                    direction)
        # print("Valid flip Row: " + str(valid_flip))

    def flipRow(self, row, column, player, opponent, opponent_prev, direction):
        possible_move = 3
        empty_space = 0
        valid_flip = False
        if (direction == 0):
            self.curr_layout, valid_flip = self.flipRow(row, column, player, opponent, opponent_prev, 1)
            self.curr_layout, valid_flip = self.flipRow(row, column, player, opponent, opponent_prev, 2)
        elif (direction == 1):
            # return if outside of board
            if (len(self.curr_layout[row]) > column > 0):
                column = column - 1
            else:
                return self.curr_layout, valid_flip
        elif (direction == 2):
            # return if outside of board
            if (len(self.curr_layout[row]) - 1 > column >= 0):
                column = column + 1
            else:
                return self.curr_layout, valid_flip
        # check if these are valid moves
        # print("row: " + str(row) + " Column: " + str(column))
        # self.print_layout()
        # print(self.curr_layout[row][column])
        if (self.curr_layout[row][column] == possible_move):
            return self.curr_layout, valid_flip
        elif (self.curr_layout[row][column] == opponent):
            opponent_prev = True
            self.curr_layout, valid_flip = self.flipRow(row, column, player, opponent, opponent_prev, direction)
            if (valid_flip):
                self.curr_layout[row][column] = player
            return self.curr_layout, valid_flip
        elif (self.curr_layout[row][column] == player and opponent_prev):
            valid_flip = True
            return self.curr_layout, valid_flip
        elif (self.curr_layout[row][column] == player):
            return self.curr_layout, valid_flip
        elif (self.curr_layout[row][column] == empty_space):
            return self.curr_layout, valid_flip

    def flipColumn(self, row, column, player, opponent, opponent_prev, direction):
        possible_move = 3
        empty_space = 0
        valid_flip = False
        if (direction == 0):
            self.curr_layout, valid_flip = self.flipColumn(row, column, player, opponent, opponent_prev, 1)
            self.curr_layout, valid_flip = self.flipColumn(row, column, player, opponent, opponent_prev, 2)
        elif (direction == 1):
            # return if outside of board
            if (len(self.curr_layout) > row > 0):
                row = row - 1
            else:
                return self.curr_layout, valid_flip
        elif (direction == 2):
            # return if outside of board
            # print(len(self.curr_layout))
            if (len(self.curr_layout) - 1 > row >= 0):
                row = row + 1
            else:
                return self.curr_layout, valid_flip
        # check if these are valid moves
        # print("Row: " + str(row))
        # print("Column: " + str(column))
        if (self.curr_layout[row][column] == possible_move):
            return self.curr_layout, valid_flip
        elif (self.curr_layout[row][column] == opponent):
            opponent_prev = True
            self.curr_layout, valid_flip = self.flipColumn(row, column, player, opponent, opponent_prev, direction)
            if (valid_flip):
                self.curr_layout[row][column] = player
            return self.curr_layout, valid_flip
        elif (self.curr_layout[row][column] == player and opponent_prev):
            valid_flip = True
            return self.curr_layout, valid_flip
        elif (self.curr_layout[row][column] == player):
            return self.curr_layout, valid_flip
        elif (self.curr_layout[row][column] == empty_space):
            return self.curr_layout, valid_flip

    def flipDiagonals(self, row, column, player, opponent, opponent_prev, direction):
        possible_move = 3
        empty_space = 0
        valid_flip = False
        # go left right etc
        if (direction == 0):
            self.curr_layout, valid_flip = self.flipDiagonals(row, column, player, opponent, opponent_prev, 1)
            self.curr_layout, valid_flip = self.flipDiagonals(row, column, player, opponent, opponent_prev, 2)
            self.curr_layout, valid_flip = self.flipDiagonals(row, column, player, opponent, opponent_prev, 3)
            self.curr_layout, valid_flip = self.flipDiagonals(row, column, player, opponent, opponent_prev, 4)
        elif (direction == 1):
            # return if outside of board
            if (len(self.curr_layout) > row > 0):
                row = row - 1
            else:
                return self.curr_layout, valid_flip
            if (len(self.curr_layout[row]) > column > 0):
                column = column - 1
            else:
                return self.curr_layout, valid_flip
        elif (direction == 2):
            # return if outside of board
            if (len(self.curr_layout) > row > 0):
                row = row - 1
            else:
                return self.curr_layout, valid_flip
            if (len(self.curr_layout[row]) - 1 > column >= 0):
                column = column + 1
            else:
                return self.curr_layout, valid_flip
        elif (direction == 3):
            # return if outside of board
            if (len(self.curr_layout) - 1 > row >= 0):
                row = row + 1
            else:
                return self.curr_layout, valid_flip
            if (len(self.curr_layout[row]) > column > 0):
                column = column - 1
            else:
                return self.curr_layout, valid_flip
        elif (direction == 4):
            # return if outside of board
            if (len(self.curr_layout) - 1 > row >= 0):
                row = row + 1
            else:
                return self.curr_layout, valid_flip
            if (len(self.curr_layout[row]) - 1 > column >= 0):
                column = column + 1
            else:
                return self.curr_layout, valid_flip
        # check if these are valid moves
        # print("Row: " + str(row))
        # print("Column: " + str(column))
        if (self.curr_layout[row][column] == possible_move):
            return self.curr_layout, valid_flip
        elif (self.curr_layout[row][column] == opponent):
            opponent_prev = True
            self.curr_layout, valid_flip = self.flipDiagonals(row, column, player, opponent, opponent_prev, direction)
            if (valid_flip):
                self.curr_layout[row][column] = player
            return self.curr_layout, valid_flip
        elif (self.curr_layout[row][column] == player and opponent_prev):
            valid_flip = True
            return self.curr_layout, valid_flip
        elif (self.curr_layout[row][column] == player):
            return self.curr_layout, valid_flip
        elif (self.curr_layout[row][column] == empty_space):
            return self.curr_layout, valid_flip
