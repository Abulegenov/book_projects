class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize static game settings"""

        #Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (233,233,233)
        

        #bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullet_difference = 15 #how distant should two bullets be
        self.bullet_amount = 15
        
        self.speedup_scale = 1.5
        self.alien_scale = 1.5
        self.alien_fleet_drop_speed = 15

        self.initialize_dynamic_settings()

        

    def initialize_dynamic_settings(self):
        #alien settings
        self.alien_speed = 5
        self.alien_fleet_direction = 1  #1 to the right, -1 to the left
        self.alien_fleet_down_check = False
        self.alien_points = 50

        #bullet settings
        self.bullet_speed = 2.5

        #ship settings
        self.ship_speed = 1.5
        self.ship_limit = 2
        
    
    def increase_speed(self):
        
        self.alien_speed*=self.speedup_scale
        self.bullet_speed*=self.speedup_scale
        self.ship_speed*=self.speedup_scale

        self.alien_points = int(self.alien_points*self.alien_scale)