import sys

import pygame

class RammieGame:
    """overall class to manage assets and behaviour"""

    def __init__(self):
        """initialize the game and create resources"""
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Ramneet's Game")
        self.bg_color = (230,230,230)

    def run_game(self):
        """start main loop for the game"""
        while True:
            #watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()


            # Redraw the screen during each pass through the loop.
            self.screen.fill(self.bg_color)

            # Make the most recent drawn screen visible

            pygame.display.flip()

if __name__ == '__main__':
    ai = RammieGame()
    ai.run_game()