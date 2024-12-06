class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize game settings"""

        #Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (233,233,233)
        self.ship_speed = 1.5

        #bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullet_difference = 15 #how distant should two bullets be
        self.bullet_amount = 6