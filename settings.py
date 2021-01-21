class Settings:
    """A class to store all settings for game project alien_invasion"""

    def __init__(self):
        """initialize all games settings."""
        # screen settings
        self.screen_width = 1920
        self.screen_height = 1080
        self.bg_colour = (0, 0, 0)

        # ship settings
        self.ship_speed = 1.5

        # Bullet settings
        self.bullet_speed = 5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 27, 0)

        # robot settings
        self.robot_speed = 1.0
        self.fleet_drop_speed = 10

        # fleet direction in the x-axis
        self.fleet_direction = 1

