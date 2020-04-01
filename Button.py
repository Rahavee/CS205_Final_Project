import pygame


class Button:

    # the constructor for the button class, with optional label
    def __init__(self, screen, color, x, y, width, height, label=""):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.label = label
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

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
