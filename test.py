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
#count = 0
#while (count < 20):
    testBoard3.generate_legal_moves()
    print("initial")
    testBoard3.print_layout()
    current_layout = testBoard3.get_current_layout()
    current_turn = testBoard3.get_current_turn()
    print("current turn: " + str(testBoard3.get_current_turn()))
    if (testBoard3.get_current_turn() == 1):
        AI1.setPossibleMove(testBoard3.isPossibleMove())
        if (testBoard3.isPossibleMove()):
            move = AI1.pick_next_move(current_layout)
            print(move)
            testBoard3.place_piece(move, current_turn)
            testBoard3.flip_pieces(move)
        testBoard3.switchTurn()
        testBoard3.print_layout()
    else:
        AI2.setPossibleMove(testBoard3.isPossibleMove())
        if (testBoard3.isPossibleMove()):
            move = AI2.pick_next_move(current_layout)
            print(move)
            testBoard3.place_piece(move, current_turn)
            testBoard3.flip_pieces(move)
        testBoard3.switchTurn()
        testBoard3.print_layout()
    #count = count + 1