import random

class opponent():
    def __init__(self, isEasy):
        self.easyDiff = isEasy
        self.possibleMove = True
        
    def pick_next_move_easy(self, gameBoard):
        currentLayout = gameBoard.get_current_layout()
        possibleMoveList = []
        possible_move = 3
        for row in range(len(currentLayout)):
            for piece in range(len(currentLayout)):
                if (currentLayout[row][piece] == possible_move):
                    columnIndex = piece
                    rowIndex = row
                    possibleMoveList.append((rowIndex, columnIndex))
        if (len(possibleMoveList) > 0):
            move = random.choice(possibleMoveList)
            gameBoard.place_piece(move[0],move[1],gameBoard.get_current_turn())
    
    def pick_next_move_difficult(self, gameBoard):
        print("Hard move")
    
    def pick_next_move(self, gameBoard):
        if (self.easyDiff):
            self.pick_next_move_easy(gameBoard)
        else:
            self.pick_next_move_difficult(gameBoard)
            
    def setPossibleMove(self, possible):
        self.possibleMove = possible
        
    def getPossibleMove(self):
        return self.possibleMove