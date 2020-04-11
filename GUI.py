import pygame
from Button import Button
from board import Board

# global variables
game = Board(2, 1)
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


# function to get the array from the backend
def updateGameArray():
    global gameArray
    gameArray = game.get_current_layout()
    # TODO: get the updated array from the backend when undo-ing a move or to see computer's move
    print(" Getting the array from the backend ")


# function to send the array to the backend
def getGameArray():
    print(" sending the gameArray ")
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
    square = 90
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
    radius = 35
    xCir = 65
    yCir = 95
    for i in range(len(gameArray)):
        for j in range(len(gameArray[i])):
            if gameArray[i][j] == 1:
                pygame.draw.circle(screen, (255, 255, 255), (xCir, yCir), radius)
            if gameArray[i][j] == 2:
                pygame.draw.circle(screen, (0, 0, 0), (xCir, yCir), radius)

            xCir = xCir + square + 1
        xCir = 65
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


def displayOtherButtons(screen):
    global otherButtons
    otherButtons = []
    otherButtons.append(Button(screen, (210, 210, 210), 900, 100, 100, 100, "Show moves"))


def eventListener(position):
    global running, gameArray, background, widthLine, flag
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
                    # TODO: Send the row and column of where the user wants to place new tile and check if that is valid
                    if game.place_piece(row, column, game.get_current_turn()):
                        # TODO: Get who is playing from the backend and pick the color of tile accordingly
                        gameArray[row][column] = game.get_current_turn()
                    # TODO: Flip the pieces
                    updateGameArray()
                    # TODO: If playing against computer then call updateGameArray() here.
            for c in range(len(bgOptions)):
                if bgOptions[c].isOver(position):
                    background = bgOptions[c].color
            for b in range(len(otherButtons)):
                if otherButtons[b].isOver(position):
                    if flag:
                        widthLine = 0
                        flag = False
                    else:
                        widthLine = 3
                        flag = True


def mainGameLoop():
    pygame.init()

    # Set up the drawing window
    screen = pygame.display.set_mode([1200, 800])

    # Run until the user asks to quit
    while running:
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

        # TODO: A check to make sure the player still has playable moves. Boolean value maybe?

    # Done! Time to quit.
    pygame.quit()


mainGameLoop()
