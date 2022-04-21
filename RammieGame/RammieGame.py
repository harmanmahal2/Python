import sys
import pygame
from bullet import Bullet
from Settings import Settings
from icon_rammie import Rammie


class RammieGame:
    """overall class to manage assets and behaviour"""

    def __init__(self):
        """initialize the game and create resources"""
        pygame.init()
        self.settings = Settings()


        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Ramneet's Game")
        self.rammie = Rammie(self) ####this is where icon_rammie gets its resources from.
        self.bullets = pygame.sprite.Group()


    def run_game(self):
        """start main loop for the game"""
        while True:
            self._check_events()
            self.rammie.update()
            self.bullets.update()

            #get rid of bullets
            self._update_screen()

            # watch for keyboard and mouse events

    def _check_events(self):
        # respond to keypress
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
               self._check_keyup_events(event)



    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.rammie.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.rammie.moving_left = True
        elif event.key == pygame.K_UP:
            self.rammie.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.rammie.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.rammie.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.rammie.moving_left = False
        if event.key == pygame.K_UP:
            self.rammie.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.rammie.moving_down = False

    def _fire_bullet(self):
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_screen(self):
        """update images on the screen, and flip to new screen"""
        self.screen.fill(self.settings.bg_color)
        self.rammie.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # Make the most recent drawn screen visible

        pygame.display.flip()


if __name__ == '__main__':
    rg = RammieGame()
    rg.run_game()
