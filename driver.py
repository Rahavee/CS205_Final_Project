import board

b = board.Board(1, 0)
first_turn = b.get_current_turn

while True:

    # TODO turn order from board
    # TODO AI player - pass layout with random moves and turn
    # TODO Tile to place from GUI

    # Get turn from player 1 and place on board
    print ("\n")
    x1,y1 = map(int, input("Player 1: row and column to play (x y)? ").split())
    b.place_piece(x1,y1,1)
    b.print_layout()
    print("Player 1 has " + str(b.get_player1_pieces()))

    # Get turn from player 2 and place on layout
    print ("\n")
    x2,y2 = map(int, input("Player 2: row and column to play (x y)? ").split())
    b.place_piece(x2,y2,2)
    b.print_layout()
    print("Player 2 has " + str(b.get_player2_pieces()))
