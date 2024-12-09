import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Class that defines the alien and it's methods"""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        
        #define the image of an alien
        self.image = pygame.image.load("images/alien.bmp")
        #define it's rectangle
        self.rect = self.image.get_rect()
        #define its position
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.settings = ai_game.settings


    def update(self):
        self.x+=self.settings.alien_speed*self.settings.alien_fleet_direction
        self.rect.x= self.x
        if self.settings.alien_fleet_down_check:
            self.y+=self.settings.alien_fleet_drop_speed
            self.rect.y = self.y
        # print(self.x)
        #if hit by bullet - delete the alien

    def check_edges(self):
        """Return true if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        return (self.rect.right>=screen_rect.right) or (self.rect.left<=0)
    
    
