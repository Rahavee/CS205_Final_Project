from board import Board

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