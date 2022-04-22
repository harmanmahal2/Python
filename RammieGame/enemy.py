import pygame
from pygame.sprite import Sprite

class Enemey(Sprite):
    ## to represent a single enemy fleet

    def __init__(self, rammie_game):
        super().__init__()
        self.screen = rammie_game.screen

        #load the alient image and get its rect

        self.image = pygame.image.load('images/enemy.png')
        self.rect = self.image.get_rect()
    #start enemy at top left
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #store exact horizontal position

        self.x = float(self.rect.x)

