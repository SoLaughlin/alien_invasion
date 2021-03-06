import pygame


class Ship:
    """A class to manage the ship"""
    def __init__(self, ai_game):
        """Initialize the ship and set its starting position"""

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        # rect = rectangle
        self.screen_rect = ai_game.screen.get_rect()

        # load the ship image and get its rect.

        self.image = pygame.image.load('images/ship_no_background.png')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        # player box will be the full range of x-axis movement on the screen but only 20% in the y-axis
        self.player_box = 0.80 * self.settings.screen_height

        # Store a decimal value for the ships horizontal position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the ships position based on the movement flag"""

        # Ensures the ship can't go off screen right
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        # Ensures the ship can't go off screen left
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # y axis_movement opposite  because of pygame starting coords (0,0) at top left of screen increasing down
        if self.moving_up and self.rect.y > self.player_box:
            self.y -= self.settings.ship_speed

        # checks that the y coordinate in ships rectangle doesnt fall below the y coordinate in the screen rect

        if self.moving_down and self.rect.midbottom[1] <= self.screen_rect.midbottom[1]:
            self.y += self.settings.ship_speed

        # updates the rectangle object from self.x
        self.rect.x = self.x

        # updates rectangle object from self.y
        self.rect.y = self.y

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)

