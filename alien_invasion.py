import sys

import pygame

from settings import Settings
from robot import Robot
from ship import Ship
from bullet import Bullet


class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        # creates a pygame surface where an element can be displayed
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.robots = pygame.sprite.Group()

        self._create_fleet()

        self.bg_colour = self.settings.bg_colour

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.bullets.update()
            self._update_robots()

    def _update_screen(self):
        """Update images on the screen and flip to the new screen"""
        # Redraw the screen during each pass through the loop
        self.screen.fill(self.settings.bg_colour)
        self.ship.blitme()
        self.robots.draw(self.screen)

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # Make the most recently drawn screen visible.
        pygame.display.flip()

    def _update_robots(self):
        """update position of all aliens in the fleet"""
        self._check_fleet_edges()
        self.robots.update()

    def _create_robot(self, robot_number, row_number):
        """Create a robot and place it in a row"""
        robot = Robot(self)
        robot_width, robot_height = robot.rect.size
        robot.x = robot_width + 2 * robot_width * robot_number
        robot.rect.x = robot.x
        robot.rect.y = robot.rect.height + 2 * robot.rect.height * row_number
        self.robots.add(robot)

    def _create_fleet(self):
        """Creates a fleet of robots"""

        robot = Robot(self)
        robot_width, robot_height = robot.rect.size

        # available space (how many robots can fit on screen on the x-axis)
        available_space_x = self.settings.screen_width - (2 * robot_width)
        number_robots_x = available_space_x // (2 * robot_width)

        # determine the number of rows of robots that fit on the screen.
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3 * robot_height) - ship_height)
        number_rows = available_space_y // (2 * robot_height)

        # create the full fleet of robots.
        for row_number in range(number_rows):
            for robot_number in range(number_robots_x):
                self._create_robot(robot_number, row_number)

    def _check_fleet_edges(self):
        """Respond by dropping down the fleet if a robot reaches an edge"""
        for robot in self.robots.sprites():
            if robot.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the direction"""
        for robot in self.robots.sprites():
            robot.rect.y += self.settings.fleet_drop_speed
            self.settings.fleet_direction *= -1

    def _check_events(self):
        """responds to keypresses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keydown presses"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True

        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True

        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True

        elif event.key == pygame.K_UP:
            self.ship.moving_up = True

        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """Respond to key releases"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False

        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

        elif event.key == pygame.K_UP:
            self.ship.moving_up = False

    def _fire_bullet(self):
        """Creates a bullet and add it to the bullets group"""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
