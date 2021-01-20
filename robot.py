import pygame
from pygame.sprite import Sprite


class Robot(Sprite):
    """Class to manage a robot character"""

    def __init__(self, ai_game):
        """initialize the robot and set its starting position"""
        super().__init__()
        self.screen = ai_game.screen

        # load the robot image and get its rect.

        self.image = pygame.image.load('images/robot_fixed.bmp')
        self.rect = self.image.get_rect()

        # Start each new robot at the middle of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)
