import board

b = board.Board(1)
current_turn = b.get_current_turn()

# IN GUI:
while True: # TODO while gameNotFinished()
    b.generate_legal_moves()
    b.print_layout()
    move_success = b.do_move()
    if(move_success):
        b.switchTurn()
