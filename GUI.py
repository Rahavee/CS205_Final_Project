import pygame
from Button import Button
from board import Board
from AI import opponent
import time

# global variables
game = Board(1, 1, 1)
defaultX = 1200
defaultY = 700
defaultScreenSize = [defaultX, defaultY]
fullScreenSize = [0,0] #set on openning of program
screenSize = defaultScreenSize
whatSize = 0 # 0 is default, 1 is fullscreen
alreadyFullScreen = False
ai = opponent(True)
tiles = []
otherButtons = []
bgOptions = []
endButtons = []
running = True
run = True
start = True
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
difficulty = 0
players = 1


# function to get the difficulty chosen. Returns 0 for easy and 1 for difficult

def getDifficulty():
    return difficulty


# function to get number of players. Returns 1 and 2
def getNumberOfPlayers():
    return players


# function to get the array from the backend
def updateGameArray():
    global gameArray
    gameArray = game.get_current_layout()
    # print(" Getting the array from the backend ")


# function to send the array to the backend
def getGameArray():
    # print(" sending the gameArray ")
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
    endButtons.append(Button(screen, (255, 255, 255), 600, 300, 100, 100, "Play again?"))
    endButtons.append(Button(screen, (210, 210, 210), 800, 500, 100, 100, "Yes"))
    endButtons.append(Button(screen, (210, 210, 210), 400, 500, 100, 100, "No"))

    if game.determineWinner() == 1:
        endButtons.append(Button(screen, (255, 255, 255), 600, 100, 100, 100, "Player 1 Wins!"))
    elif game.determineWinner() == 2:
        endButtons.append(Button(screen, (255, 255, 255), 600, 100, 100, 100, "Player 2 Wins"))
    elif game.determineWinner() == 3:
        endButtons.append(Button(screen, (255, 255, 255), 600, 100, 100, 100, "It's a tie!"))


def displayOtherButtons(screen):
    global otherButtons
    otherButtons = []
    otherButtons.append(Button(screen, (210, 210, 210), 950, 100, 100, 100, "Show moves"))
    otherButtons.append(Button(screen, (210, 210, 210), 950, 200, 100, 100, "Help"))
    otherButtons.append(Button(screen, (210, 210, 210), 750, 100, 100, 100, "Fullscreen"))
    otherButtons.append(Button(screen, (210, 210, 210), 750, 200, 100, 100, "Default Screen Size"))
    player1Tiles = "Player 1 tiles = " + str(game.numberOfTiles(1))
    player2Tiles = "Player 2 tiles = " + str(game.numberOfTiles(2))
    otherButtons.append(Button(screen, (255, 255, 255), 900, 500, 100, 100, player1Tiles))
    otherButtons.append(Button(screen, (255, 255, 255), 900, 600, 100, 100, player2Tiles))


# Returns the players moves
def getNextMove():
    return row, column


def eventListener(position):
    global running, gameArray, background, widthLine, flag, row, column, run, screenSize, whatSize, alreadyFullScreen, start
    for event in pygame.event.get():
        # Did the user click the window close button?
        if event.type == pygame.QUIT:
            running = False
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        # Did the user click?
        if event.type == pygame.MOUSEBUTTONDOWN:
            for t in range(len(tiles)):
                if tiles[t].isOver(position):
                    row = t // 8
                    column = t % 8
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
            if otherButtons[2].isOver(position):
                screenSize = fullScreenSize
                whatSize = 1
            if otherButtons[3].isOver(position):
                screenSize = defaultScreenSize
                whatSize = 0
                alreadyFullScreen = False

            try:
                if endButtons[1].isOver(position):
                    game.reset()
                    start = True
                    mainGameLoop()
                if endButtons[2].isOver(position):
                    running = False
                    run = False
            except:
                pass


def mainGameLoop():
    global screenSize, fullScreenSize, whatSize, alreadyFullScreen, running
    pygame.init()
    flagEnd = False

    infoObject = pygame.display.Info()
    fullScreenSize = [infoObject.current_w, infoObject.current_h]
    # Set up the drawing window
    if whatSize == 0:
        screen = pygame.display.set_mode(screenSize)
    else:
        screen = pygame.display.set_mode([0,0], pygame.FULLSCREEN)
    # Run until the user asks to quit

    while running:
        if whatSize == 0:
            screen = pygame.display.set_mode(screenSize)
        else:
            if alreadyFullScreen == False:
                alreadyFullScreen = True
                screen = pygame.display.set_mode([0,0], pygame.FULLSCREEN)

        # Fill the background with white
        screen.fill((255, 255, 255))

        if start:
            startScreen(screen)
        else:
            if not flagEnd:
                print(difficulty, players)

                # Draw the screen elements
                drawBoard(screen)
                displayOtherButtons(screen)
                changeBackground(screen)
                pygame.display.update()

                # get the mouse position and check whether there was a click
                position = pygame.mouse.get_pos()
                eventListener(position)

                # Game operations
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
                endScreen()
        # Flip the display
        pygame.display.flip()

    # Done! Time to quit.
    pygame.quit()


def startScreen(screen):
    global difficulty, players, start, running
    banner = pygame.image.load("gameBanner.jpg")
    screen.blit(banner, (10, 10))
    diff = []
    people = []
    Button(screen, (255, 255, 255), 200, 300, 100, 100, "Difficulty")
    diff.append(Button(screen, (210, 210, 210), 100, 400, 100, 100, "Easy"))
    diff.append(Button(screen, (210, 210, 210), 300, 400, 100, 100, "Difficult"))

    Button(screen, (255, 255, 255), 900, 300, 100, 100, "Players")
    people.append(Button(screen, (210, 210, 210), 800, 400, 100, 100, "1"))
    people.append(Button(screen, (210, 210, 210), 1000, 400, 100, 100, "2"))
    close = Button(screen, (210, 210, 210), 500, 600, 100, 100, "Game")

    position = pygame.mouse.get_pos()

    for event in pygame.event.get():
        # Did the user click the window close button?
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

        # Did the user click?
        if event.type == pygame.MOUSEBUTTONDOWN:
            if diff[0].isOver(position):
                difficulty = 0

            if diff[1].isOver(position):
                difficulty = 1

            if people[0].isOver(position):
                players = 1

            if people[1].isOver(position):
                players = 2
            if close.isOver(position):
                start = False

    pygame.display.update()


def endScreen():
    global alreadyFullScreen
    pygame.init()
    run = True
    if whatSize == 0:
        end = pygame.display.set_mode(screenSize)
        alreadyFullScreen = False
    else:
        end = pygame.display.set_mode([0,0], pygame.FULLSCREEN)
        alreadyFullScreen = True
    while run:
        if whatSize == 0:
            end = pygame.display.set_mode(screenSize)
        else:
            if alreadyFullScreen == False:
                alreadyFullScreen = True
                end = pygame.display.set_mode([0,0], pygame.FULLSCREEN)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
        end.fill((255,255,255))
        displayEndButtons(end)
        pygame.display.update()
        position = pygame.mouse.get_pos()
        eventListener(position)


def helpScreen():
    global alreadyFullScreen
    pygame.init()

    # Set up the drawing window
    if whatSize == 0:
        help = pygame.display.set_mode(screenSize)
        alreadyFullScreen = False
    else:
        help = pygame.display.set_mode([0,0], pygame.FULLSCREEN)
        alreadyFullScreen = True
    # Run until the user asks to quit
    run = True
    while run:
        if whatSize == 0:
            help = pygame.display.set_mode(screenSize)
            alreadyFullScreen = False
        else:
            if alreadyFullScreen == False:
                help = pygame.display.set_mode([0,0], pygame.FULLSCREEN)
        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False

        # Fill the background with white
        help.fill((255, 255, 255))

        # Write out the text
        font = pygame.font.SysFont('comicsans', 30)
        rules = "Othello Rules\nGame setup:\nThe game is played on an 8x8 grid. There are two color pieces (black or " \
                "white) to designate either player 1 or player 2. The two players that are trying to claim as much of " \
                "the board as possible with their designated pieces.\nGame Start:\nTo start the game place 4 pieces " \
                "in a diagonal pattern as seen in the photo below\n"
        picture = pygame.image.load("startBoard.gif")
        help.blit(picture, (30, 190))
        rules2 = "Game Capture:\nIn " \
                 "order to capture the opponents pieces it must be between your most recent placed piece and a " \
                 "previously placed piece of the same color. The capture can occur horizontally, vertically, " \
                 "and diagonally. If you are confused as to what a legal move is turn on the feature that shows all " \
                 "legal moves on the game board.\nGame Finish:\nThe Game is finished when neither player has a legal " \
                 "move, or one of the players resigns. The winner of the game is the player with the most pieces on " \
                 "the board, unless a player resigned. The player that resigns loses the game "

        myRect = pygame.Rect((20, 20, 1000, 160))
        myRect2 = pygame.Rect((20, 20, 1000, 400))

        text = renderText(rules, font, myRect, (0, 0, 0), (255, 255, 255), 0)
        text2 = renderText(rules2, font, myRect2, (0, 0, 0), (255, 255, 255), 0)

        if text:
            help.blit(text, myRect.topleft)
            help.blit(text2,myRect2.bottomleft)

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
