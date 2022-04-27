import pygame
from pygame.sprite import Sprite

class Enemy(Sprite):
    ## to represent a single enemy fleet

    def __init__(self, rammie_game):
        super().__init__()
        self.screen = rammie_game.screen
        self.settings = rammie_game.settings

        #load the alient image and get its rect

        self.image = pygame.image.load('images/enemy.png')
        self.rect = self.image.get_rect()
    #start enemy at top left
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #store exact horizontal position

        self.x = float(self.rect.x)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        self.x += self.settings.rammie_speed * self.settings.fleet_direction
        self.rect.x = self.x




