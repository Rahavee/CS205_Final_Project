import pygame
from Button import Button
from board import Board
from AI import opponent
import time

# global variables
game = Board(1, 1, 1)
ai = opponent(True)
tiles = []
otherButtons = []
bgOptions = []
running = True
gameArray = []
green = (34, 139, 34)
blue = (34, 34, 139)
red = (139, 34, 34)
purple = (128, 0, 128)
background = green
widthLine = 0
flag = False
row = 0
column = 0


# function to get the array from the backend
def updateGameArray():
    global gameArray
    gameArray = game.get_current_layout()
    # TODO: get the updated array from the backend when undo-ing a move or to see computer's move
    # print(" Getting the array from the backend ")


# function to send the array to the backend
def getGameArray():
    # print(" sending the gameArray ")
    # TODO: Send the matrix to the backend
    return gameArray


# function to draw the 8x8 board and the pieces
def drawBoard(screen):
    global tiles
    updateGameArray()
    tiles = []
    # To draw the grid squares
    x = 20
    y = 50
    square = 80
    for i in range(0, 8):
        for j in range(0, 8):
            if gameArray[i][j] == 3:
                color = background
                if flag:
                    color = (0, 0, 0)

                tiles.append(Button(screen, color, x, y, square, square, widthLine=widthLine))
            else:
                tiles.append(Button(screen, background, x, y, square, square))
            x = x + square + 1
        x = 20
        y = y + square + 1

    # drawing the playing pieces
    radius = 30
    xCir = 60
    yCir = 90
    for i in range(len(gameArray)):
        for j in range(len(gameArray[i])):
            if gameArray[i][j] == 1:
                pygame.draw.circle(screen, (255, 255, 255), (xCir, yCir), radius)
            if gameArray[i][j] == 2:
                pygame.draw.circle(screen, (0, 0, 0), (xCir, yCir), radius)

            xCir = xCir + square + 1
        xCir = 60
        yCir = yCir + square + 1


# buttons for changing the background color
def changeBackground(screen):
    global bgOptions
    bgOptions = []
    Button(screen, (255, 255, 255), 900, 300, 100, 100, "background color")
    bgOptions.append(Button(screen, red, 800, 400, 30, 30))
    bgOptions.append(Button(screen, blue, 840, 400, 30, 30))
    bgOptions.append(Button(screen, purple, 880, 400, 30, 30))
    bgOptions.append(Button(screen, green, 920, 400, 30, 30))


def displayEndButtons(screen):
    global endButtons
    endButtons = []
    endButtons.append(Button(screen, (210, 210, 210), 600, 200, 100, 100, "Play again?"))
    endButtons.append(Button(screen, (210, 210, 210), 800, 600, 100, 100, "Yes"))
    endButtons.append(Button(screen, (210, 210, 210), 400, 600, 100, 100, "No"))


def displayOtherButtons(screen):
    global otherButtons
    otherButtons = []
    otherButtons.append(Button(screen, (210, 210, 210), 900, 100, 100, 100, "Show moves"))
    otherButtons.append(Button(screen, (210, 210, 210), 900, 200, 100, 100, "Help"))


# Returns the players moves
def getNextMove():
    return row, column


def eventListener(position):
    global running, gameArray, background, widthLine, flag, row, column
    for event in pygame.event.get():
        # Did the user click the window close button?
        if event.type == pygame.QUIT:
            running = False
        # Did the user click?
        if event.type == pygame.MOUSEBUTTONDOWN:
            for t in range(len(tiles)):
                if tiles[t].isOver(position):
                    row = t // 8
                    column = t % 8
                    # TODO: Get who is playing from the backend and pick the color of tile accordingly
                    # updateGameArray()
            for c in range(len(bgOptions)):
                if bgOptions[c].isOver(position):
                    background = bgOptions[c].color

            if otherButtons[0].isOver(position):
                if flag:
                    widthLine = 0
                    flag = False
                else:
                    widthLine = 3
                    flag = True
            if otherButtons[1].isOver(position):
                helpScreen()
            # try:
            #     # TODO: Start New Game
            #     # if endButtons[1].isOver(position):
            #
            #     if endButtons[2].isOver(position):
            #         running = False
            # except:
            #     pass


def mainGameLoop():
    pygame.init()
    flagEnd = False

    # Set up the drawing window
    screen = pygame.display.set_mode([1200, 700])

    # Run until the user asks to quit
    while running:
        if not flagEnd:
            # Fill the background with white
            screen.fill((255, 255, 255))

            # Draw the screen elements
            drawBoard(screen)
            displayOtherButtons(screen)
            changeBackground(screen)
            pygame.display.update()

            # get the mouse position and check whether there was a click
            position = pygame.mouse.get_pos()
            eventListener(position)

            # Flip the display
            pygame.display.flip()

            # Game operations
            # TODO check end condition - both players have no legal moves
            game.generate_legal_moves()

            # If player 1's turn and legal moves exist
            if (game.get_current_turn() == 1 and game.isPossibleMove()):
                if (game.place_piece((row, column), 1)):
                    game.flip_pieces((row, column))
                    game.switchTurn()


            # If player 2's turn and legal moves exist
            elif (game.get_current_turn() == 2 and ai.getPossibleMove()):  # If player 2's turn
                move = ai.pick_next_move(game.get_current_layout())
                time.sleep(1)
                if (game.place_piece(move, 2)):  # Returns True if place_piece succeeds
                    game.flip_pieces(move)
                    game.switchTurn()

            else:
                flagEnd = True


        # Neither player has legal moves, game is over
        else:
            # TODO GUI solution to this
            print("game over")
            screen.fill((255, 255, 255))
            displayEndButtons(screen)
            pygame.display.update()
            position = pygame.mouse.get_pos()
            eventListener(position)

    # Done! Time to quit.
    pygame.quit()


def helpScreen():
    pygame.init()

    # Set up the drawing window
    global help
    help = pygame.display.set_mode([1200, 700])

    # Run until the user asks to quit
    run = True
    while run:

        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Fill the background with white
        help.fill((255, 255, 255))

        # Write out the text
        font = pygame.font.SysFont('comicsans', 30)
        rules = "Reversi Rules\nGame setup:\nThe game is played on an 8x8 grid. There are two color pieces (black or " \
                "white) to designate either player 1 or player 2. The two players that are trying to claim as much of " \
                "the board as possible with their designated pieces.\nGame Start:\nTo start the game place 4 pieces " \
                "in a diagonal pattern as seen in the photo below\n_Add_Photo_Of_Game_Start_\nGame Capture:\n	In " \
                "order to capture the opponents pieces it must be between your most recent placed piece and a " \
                "previously placed piece of the same color. The capture can occur horizontally, vertically, " \
                "and diagonally. If you are confused as to what a legal move is turn on the feature that shows all " \
                "legal moves on the game board.\nGame Finish:\nThe Game is finished when neither player has a legal " \
                "move, or one of the players resigns. The winner of the game is the player with the most pieces on " \
                "the board, unless a player resigned. The player that resigns loses the game "


        myRect = pygame.Rect((20, 20, 800, 800))

        text = renderText(rules, font, myRect, (0, 0, 0), (255, 255, 255), 0)

        if text:
            help.blit(text, myRect.topleft)

        pygame.display.update()


# Code in the following function authored by http://www.pygame.org/pcr/text_rect/index.php
def renderText(string, font, rect, text_color, background_color, justification=0):
    final_lines = []

    requested_lines = string.splitlines()

    # Create a series of lines that will fit on the provided
    # rectangle.

    for requested_line in requested_lines:
        if font.size(requested_line)[0] > rect.width:
            words = requested_line.split(' ')
            # Start a new line
            accumulated_line = ""
            for word in words:
                test_line = accumulated_line + word + " "
                # Build the line while the words fit.
                if font.size(test_line)[0] < rect.width:
                    accumulated_line = test_line
                else:
                    final_lines.append(accumulated_line)
                    accumulated_line = word + " "
            final_lines.append(accumulated_line)
        else:
            final_lines.append(requested_line)

            # Let's try to write the text out on the surface.

    surface = pygame.Surface(rect.size)
    surface.fill(background_color)

    accumulated_height = 0
    for line in final_lines:
        if line != "":
            tempsurface = font.render(line, 1, text_color)
            if justification == 0:
                surface.blit(tempsurface, (0, accumulated_height))
            elif justification == 1:
                surface.blit(tempsurface, ((rect.width - tempsurface.get_width()) / 2, accumulated_height))
            elif justification == 2:
                surface.blit(tempsurface, (rect.width - tempsurface.get_width(), accumulated_height))
        accumulated_height += font.size(line)[1]

    return surface


mainGameLoop()
