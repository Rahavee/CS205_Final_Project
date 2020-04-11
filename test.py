from board import Board
from AI import opponent

testBoard1 = Board(1, 1, 1)
testBoard2 = Board(1, 1, 1)
testBoard3 = Board(1, 1, 1)

#generate boards
print("Test Board 1: Before")
testBoard1.print_layout()
testBoard1.curr_layout = [
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,1,2,0,0,0],
            [0,0,0,2,1,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0]]
testBoard1.generate_legal_moves()
print("Test Board 1: After")
testBoard1.print_layout()


print("Test Board 2: Before")
testBoard2.curr_layout = [
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,2,0,0],
            [0,0,1,1,2,0,0,0],
            [0,0,1,2,1,0,0,0],
            [0,0,2,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0]]
testBoard2.print_layout()
testBoard2.generate_legal_moves()
print("Test Board 2: After")
testBoard2.print_layout()

print("Play Computer PLAY!!")
AI1 = opponent(True)
AI2 = opponent(True)
testBoard3.generate_legal_moves()
while (AI1.getPossibleMove() and AI2.getPossibleMove()):
    testBoard3.generate_legal_moves()
    print("current turn: " + str(testBoard3.get_current_turn()))
    if (testBoard3.get_current_turn() == 1):
        AI1.setPossibleMove(testBoard3.isPossibleMove())
        AI1.pick_next_move(testBoard3)
        testBoard3.switchTurn()
        testBoard3.print_layout()
    else:
        AI1.setPossibleMove(testBoard3.isPossibleMove())
        AI2.pick_next_move(testBoard3)
        testBoard3.switchTurn()
        testBoard3.print_layout()