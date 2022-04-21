import pygame


class Rammie:

    def __init__(self, rammie_game):
        self.screen = rammie_game.screen
        self.settings = rammie_game.settings
        self.screen_rect = rammie_game.screen.get_rect()

        self.image = pygame.image.load('images/rammie.png')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

        #self.x = float(self.rect.x)
        #self.y = float(self.rect.y)

        self.rect.x = float(self.rect.x)
        self.rect.y = float(self.rect.y)

        #movement flag

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):


        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.settings.rammie_speed

        if self.moving_left and self.rect.left > 0:
            self.rect.x -= self.settings.rammie_speed

        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += self.settings.rammie_speed

        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.rect.y -= self.settings.rammie_speed

        #self.rect.x = self.x
        #self.rect.y = self.y

        # i modifield this code to minimize the logic. Assigned float value to self.rect.x and y originally


    def blitme(self):
        self.screen.blit(self.image, self.rect)