import pygame

gameArray = [[2, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 4, 0, 0, 0], [0, 0, 0, 2, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 2, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]


# function to get the array from the backend
def updateGameArray():
    global gameArray


# function to send the array to the backend
def getGameArray():
    return gameArray


# function to draw the 8x8 board and the pieces
def drawBoard():
    global gameArray
    # To draw the grid squares
    x = 20
    y = 50
    square = 90
    for i in range(0, 8):
        for j in range(0, 8):
            pygame.draw.rect(screen, (0, 0, 255), (x, y, square, square))
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
                pygame.draw.circle(screen, (0, 255, 0), (xCir, yCir), radius)
            if gameArray[i][j] == 2:
                pygame.draw.circle(screen, (255, 0, 0), (xCir, yCir), radius)
            xCir = xCir + square +1
        xCir = 65
        yCir = yCir + square + 1


def mainGameLoop():
    pygame.init()

    # Set up the drawing window
    global screen
    screen = pygame.display.set_mode([1000, 800])

    # Run until the user asks to quit
    running = True
    while running:

        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the background with white
        screen.fill((255, 255, 255))

        drawBoard()

        # Flip the display
        pygame.display.flip()

    # Done! Time to quit.
    pygame.quit()


mainGameLoop()
