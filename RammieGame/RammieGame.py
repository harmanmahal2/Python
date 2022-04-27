import sys
import pygame
from bullet import Bullet
from Settings import Settings
from icon_rammie import Rammie
from enemy import Enemy


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
        self.enemies = pygame.sprite.Group()
        self._create_fleet()






    def _create_fleet(self):
        #make aliens
        enemy = Enemy(self)
        enemy_width, enemy_height = enemy.rect.size
        available_space_x = self.settings.screen_width - (2 * enemy_width)
        number_enemies_x = available_space_x // (2 * enemy_width)


            #determine number of rows

        rammie_height = self.rammie.rect.height
        available_space_y = (self.settings.screen_height - (3 * enemy_height) - rammie_height)
        number_rows = available_space_y // (2 * enemy_height)

        for row_number in range(number_rows):
            for enemy_number in range(number_enemies_x):
                self._create_enemy(enemy_number, row_number)

        #create the first row of aliens


    def _create_enemy(self, enemy_number, row_number):

            enemy = Enemy(self)
            enemy_width, enemy_height = enemy.rect.size
            enemy.x = enemy_width + 2 * enemy_width * enemy_number
            enemy.rect.x = enemy.x
            enemy.rect.y = enemy.rect.height + 2 * enemy.rect.height * row_number
            self.enemies.add(enemy)



    def _check_fleet_edges(self):
        ##respond app. if enemies touch the edge"
        for enemy in self.enemies.sprites():
            if enemy.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        for enemy in self.enemies.sprites():
            enemy.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1



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
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)






    def _update_screen(self):
        """update images on the screen, and flip to new screen"""
        self.screen.fill(self.settings.bg_color)
        self.rammie.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.enemies.draw(self.screen)







    def _update_bullets(self):
        self.bullets.update()

        #get rid of old bullets
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)



    def _update_enemy(self):
        self._check_fleet_edges()
        self.enemies.update()



        # Make the most recent drawn screen visible

        pygame.display.flip()






    def run_game(self):
        """start main loop for the game"""
        while True:
            self._check_events()
            self.rammie.update()
            self._update_bullets()
            self._update_enemy()
            self._update_screen()




if __name__ == '__main__':
    rg = RammieGame()
    rg.run_game()
