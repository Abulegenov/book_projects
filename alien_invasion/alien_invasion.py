import sys
from time import sleep
import pygame
from settings import Settings
from ship import Ship
from new_item import NewItem
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

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
        self.stats = GameStats(self)

        self.ship = Ship(self)
        # self.new_item = NewItem(self)
        self.bullets = pygame.sprite.Group()
        self.shooting = False

        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        
        self.game_active = False
        self.play_button = Button(self,'Play')
        self.scoreboard = Scoreboard(self)




    def run_game(self):
        """Start the main loop for the game"""
        while True:
            #watch for keyboard and mouse events.
            self._check_events()
            if self.game_active:
                self.ship.update()
                self._create_bullets()
                self._update_bullets()
                self._update_aliens()
            

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
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        #Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)

        
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)
        self.scoreboard.show_score()
        # self.new_item.blitme()
        if not self.game_active:
            self.play_button.draw_button()
        
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
            
    def _update_bullets(self):
        """Check if two bullets fired one after another without waiting to be fired fully"""
        """Also check if bullets are out of screen"""
        self.bullets.update()
        self._regulate_bullets()
        self._delete_bullets_edged()
        self._check_bullet_alien_collisions()
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
        

    def _regulate_bullets(self):
        to_delete = []
        if len(self.bullets)>1:
            list_bullets = list(self.bullets)
            for i in range(len(self.bullets)-1):
                if list_bullets[i+1].rect.top-list_bullets[i].rect.bottom<self.settings.bullet_difference:
                    to_delete.append(list_bullets[i+1])
            for bullet in to_delete:
                self.bullets.remove(bullet)

    def _delete_bullets_edged(self):
        for bullet in self.bullets.copy():
            if bullet.rect.bottom<=0:
                self.bullets.remove(bullet)

    def _check_bullet_alien_collisions(self):
        collisions = pygame.sprite.groupcollide(self.bullets,self.aliens, True, True)
        if collisions:
            for aliens in collisions.values():
                self.stats.update_alien_destroyed(len(aliens))
            self.scoreboard.prep_score()
            self.scoreboard.check_high_score()
        if not self.aliens:
            self.bullets.empty()
            self.aliens.empty()
            self._create_fleet()
            # self.settings.increase_speed()
            self.stats.level+=1
            self.scoreboard.prep_level()
        
            
    def _create_fleet(self):
        """Create the fleet of aliens"""
        
        alien_amount = int(self.settings.screen_width/(2*Alien(self).rect.width))
        row_numbers = int((self.settings.screen_height)/(3*Alien(self).rect.width))
        for row in range(row_numbers):  
            for i in range(alien_amount-1):
                alien = Alien(self)
                alien.rect.x = alien.rect.x+ alien.rect.width*i +alien.rect.x*i
                alien.rect.y = alien.rect.y + alien.rect.height*row +alien.rect.y*row
                alien.x = alien.rect.x
                alien.y = alien.rect.y
                self.aliens.add(alien)
    
    def _update_aliens(self):
        """Update the movement of aliens"""
        
        self.settings.alien_fleet_down_check = False
        for alien in self.aliens:
            if alien.check_edges():
                self.settings.alien_fleet_direction *= (-1)
                self.settings.alien_fleet_down_check = True
                break
        self.aliens.update()

        # Look for alien-ship collisions.
        if pygame.sprite.spritecollideany(self.ship,self.aliens):
            # print("Ship hit")
            self._ship_hit()

        self._check_aliens_bottom()
    
    def _ship_hit(self):
        """Respond to the ship being hit by an alien"""

        self.stats.ships_left-=1

        self.bullets.empty()
        self.aliens.empty()

        if self.stats.ships_left<0:
            self.game_active = False
            pygame.mouse.set_visible(True)

        else:
            self.settings.increase_speed()
            self._create_fleet()
            self.ship.center_ship()
            self.stats.level+=1
            self.scoreboard.prep_level()
            self.scoreboard.prep_ships()

            sleep(0.5)

    def _check_aliens_bottom(self):
        """Check if any alien reached the bottom of the screen"""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                self._ship_hit()

    def _check_play_button(self,mouse_pos):
        if self.play_button.rect.collidepoint(mouse_pos) and not self.game_active:
            self.stats.reset_stats()
            self.scoreboard.prep_score()
            self.scoreboard.prep_level()
            self.scoreboard.prep_ships()
            self.game_active = True
             # Get rid of any remaining bullets and aliens.
            self.bullets.empty()
            self.aliens.empty()
            # Create a new fleet and center the ship.
            self.ship.center_ship()
            self.settings.initialize_dynamic_settings()
            self._create_fleet()
            
            pygame.mouse.set_visible(False)

if __name__=='__main__':
    #Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()