import pygame
from Button import Button

# global variables
tiles = []
running = True
gameArray = [[0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 2, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 2, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]


# function to get the array from the backend
def updateGameArray():
    global gameArray
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
    tiles = []
    # To draw the grid squares
    x = 20
    y = 50
    square = 90
    for i in range(0, 8):
        for j in range(0, 8):
            tiles.append(Button(screen, (0, 255, 0), x, y, square, square))
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
                pygame.draw.circle(screen, (50, 0, 0), (xCir, yCir), radius)
            if gameArray[i][j] == 2:
                pygame.draw.circle(screen, (255, 0, 0), (xCir, yCir), radius)
            xCir = xCir + square + 1
        xCir = 65
        yCir = yCir + square + 1


def eventListener(position):
    global running, gameArray
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
                    # TODO: Get who is playing from the backend and pick the color of tile accordingly
                    gameArray[row][column] = 1
                    # TODO: If playing against computer then call updateGameArray() here


def mainGameLoop():
    pygame.init()

    # Set up the drawing window
    screen = pygame.display.set_mode([1000, 800])

    # Run until the user asks to quit
    while running:
        # Fill the background with white
        screen.fill((255, 255, 255))

        # Draw the screen elements
        drawBoard(screen)
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
