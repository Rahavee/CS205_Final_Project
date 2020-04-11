import random

class opponent():
    def __init__(self, isEasy):
        self.easyDiff = isEasy
        self.possibleMove = True
        
    def pick_next_move_easy(self, gameBoard):
        currentLayout = gameBoard
        possibleMoveList = []
        possible_move = 3
        for row in range(len(currentLayout)):
            for piece in range(len(currentLayout)):
                #print(currentLayout[row][piece])
                if (currentLayout[row][piece] == possible_move):
                    columnIndex = piece
                    rowIndex = row
                    #print("Row: " + str(rowIndex) + " Column: " + str(columnIndex))
                    possibleMoveList.append((rowIndex, columnIndex))
        if (len(possibleMoveList) > 0):
            move = random.choice(possibleMoveList)
            #print(move)
            return move
    
    def pick_next_move_difficult(self, gameBoard):
        print("Hard move")
    
    def pick_next_move(self, gameBoard):
        if (self.easyDiff):
            return self.pick_next_move_easy(gameBoard)
        else:
            return self.pick_next_move_difficult(gameBoard)
            
    def setPossibleMove(self, possible):
        self.possibleMove = possible
        
    def getPossibleMove(self):
        return self.possibleMove