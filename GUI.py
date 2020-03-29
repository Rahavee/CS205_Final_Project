import pygame

# function to get the array from the backend
def updateGameArray():
    global gameArray
    gameArray = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]


# function to send the array to the backened
def getGameArray():
    return gameArray


# function to draw the 8x8 board and the pieces
def drawBoard():
    x = 20
    y = 50
    for i in range(0,7):
        for j in range(0,7):
            pygame.draw.rect(screen, (0, 0, 255), (x, y, 90, 90))
            x = x + 91
        x = 20
        y = y + 91


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