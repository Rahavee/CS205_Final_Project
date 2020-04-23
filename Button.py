import pygame


class Button:

    # the constructor for the button class, with optional label
    def __init__(self, screen, color, x, y, width, height, label="", widthLine=0):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.label = label
        pygame.init()
        pygame.font.init()
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), widthLine)
        if self.label != '':
            font = pygame.font.SysFont('comicsans', 30)
            text = font.render(self.label, 1, (0, 0, 0))
            screen.blit(text, (
                self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    # to get the center of the button
    def getCenter(self):
        self.centerX = self.x + self.width / 2
        self.centerY = self.y + self.height / 2
        return self.centerX

    # to check if the mouse is over the button
    def isOver(self, mouse):
        if self.x < mouse[0] < self.x + self.width:
            if self.y < mouse[1] < self.y + self.height:
                return True
        return False
