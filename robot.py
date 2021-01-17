import pygame


class Robot:
    """Class to manage a robot character"""
    def __init__(self, ai_game):
        """initialize the robot and set its starting position"""
        self.screen = ai_game.screen
        # rect = rectangle
        self.screen_rect = ai_game.screen.get_rect()

        # load the ship image and get its rect.

        self.image = pygame.image.load('images/robot char resized.bmp')
        self.rect = self.image.get_rect()

        # Start each new robot at the middle of the screen
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)
