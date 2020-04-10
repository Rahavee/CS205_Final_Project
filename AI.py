

class opponent():
    def __init__(self, isEasy):
        self.easyDiff = isEasy
        
    def pick_next_move_easy(self, gameBoard):
        currentLayout = gameBoard.get_current_layout()
        possibleMoveList = []
        possible_move = 3
        for row in currentLayout:
            for piece in row:
                if (piece == possible_move):
                    columnIndex = row.index(piece)
                    rowIndex = self.curr_layout.index(row)
                    possibleMoveList.append((rowIndex, columnIndex))
        move = possibleMoveList
        gameBoard.changePiece(move)
    
    def pick_next_move_difficult(self, gameBoard):
        print("Hard move")
    
    def pick_next_move(self, gameBoard):
        if (self.easyDiff):
            self.pick_next_move_easy(gameBoard)
        else:
            self.pick_next_move_difficult(gameBoard)