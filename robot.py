import pygame
from pygame.sprite import Sprite


class Robot(Sprite):
    """Class to manage a robot character"""

    def __init__(self, ai_game):
        """initialize the robot and set its starting position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # load the robot image and get its rect.

        self.image = pygame.image.load('images/robot_fixed.png')
        self.rect = self.image.get_rect()

        # Start each new robot at the middle of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def update(self):
        """move the alien to the right or left"""
        self.x += (self.settings.robot_speed * self.settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        """Returns true if a robot is at the edge of the screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
