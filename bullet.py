import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Class to manage bullets fired from the ship"""

    def __init__(self, ai_game):
        """Create a bullet object at the ships curren't position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.colour = self.settings.bullet_color

        # create a rect for a bullet
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_width)
        # set the bullets starting position at the midtop of the ship
        self.rect.midtop = ai_game.ship.rect.midtop

        # store the bullets position as a decimal value.
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen."""
        # decimal position of the bullet
        self.y -= self.settings.bullet_speed

        # update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen"""
        pygame.draw.rect(self.screen, self.settings.bullet_color, self.rect)

