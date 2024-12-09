import pygame
import pygame.font as ft

class Button:
    """A class to built buttons for the game."""

    def __init__(self,ai_game,msg):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        "Dimensions and properties of the button"
        self.width, self.height = 200,50
        self.button_color = (200,200,200)
        self.text_color = (100,100,100)
        self.font = ft.SysFont(None,48)

        "Building the button"
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = self.screen_rect.center

        self._prep_msg(msg)
    
    def _prep_msg(self, msg):
        """Turn the msg into a rendered image and center text on the button."""
        self.msg_image = self.font.render(msg,True,self.text_color,self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
    
    def draw_button(self):
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)


