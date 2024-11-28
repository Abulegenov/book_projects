import sys
import pygame
from settings import Settings
from ship import Ship
from new_item import NewItem
from bullet import Bullet


class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources"""
        pygame.init()
        self.settings = Settings()
    
        # self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        # self.settings.screen_width,self.settings.screen_height = self.screen.get_rect().width, self.screen.get_rect().height
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))

        pygame.display.set_caption("Alien Invasion")
        self.clock = pygame.time.Clock()
        self.ship = Ship(self)
        # self.new_item = NewItem(self)
        self.bullets = pygame.sprite.Group()
        self.shooting = False

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            #watch for keyboard and mouse events.
            self._check_events()
            self.ship.update()
            self._create_bullets()
            self.bullets.update()
            self._check_delete_bullets()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    #Move the ship to the right.
                    self.ship.moving_right = True

                elif event.key == pygame.K_LEFT:
                    #Move the ship to the right.
                    self.ship.moving_left = True
                    
                elif event.key == pygame.K_UP:
                    #Move the ship to the right.
                    self.ship.moving_up = True
                    
                elif event.key == pygame.K_DOWN:
                    #Move the ship to the right.
                    self.ship.moving_down = True
                elif event.key == pygame.K_q:
                    sys.exit()
                elif event.key == pygame.K_SPACE:
                    self.shooting = True
                    

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False
                elif event.key == pygame.K_UP:
                    self.ship.moving_up = False
                elif event.key == pygame.K_DOWN:
                    self.ship.moving_down = False
                elif event.key == pygame.K_SPACE:
                    self.shooting = False

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        #Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)

        
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        # self.new_item.blitme()
        
        #Make the most recently drawn screen visible
        pygame.display.flip()
    
    def _fire_bullet(self):
        """Fires a bullet"""
        if len(self.bullets)<self.settings.bullet_amount:
            new_bullet = Bullet(self)
            new_bullet.y = self.ship.rect.top
            new_bullet.x = self.ship.rect.center[0]
            self.bullets.add(new_bullet)
        # new_bullet.y = self.ship.rect.top
        # new_bullet.draw_bullet()
    
    def _create_bullets(self):
        """Creates bullets"""
        if self.shooting:
            self._fire_bullet()
            
    def _check_delete_bullets(self):
        """Check if two bullets fired one after another without waiting to be fired fully"""
        """Also check if bullets are out of screen"""
        to_delete = []
        if len(self.bullets)>1:
            list_bullets = list(self.bullets)
            for i in range(len(self.bullets)-1):
                if list_bullets[i+1].rect.top-list_bullets[i].rect.bottom<self.settings.bullet_difference:
                    to_delete.append(list_bullets[i+1])
            for bullet in to_delete:
                self.bullets.remove(bullet)
            for bullet in self.bullets.copy():
                if bullet.rect.bottom<=0:
                    self.bullets.remove(bullet)
            





if __name__=='__main__':
    #Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()