# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidFields

class GameCtrl:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.updatable = pygame.sprite.Group()
        self.drawable = pygame.sprite.Group()
        self.asteroids = pygame.sprite.Group()
        self.clock = pygame.time.Clock()
        self.dt = 0


def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    game = GameCtrl()
    
    Asteroid.containers = (game.asteroids, game.updatable, game.drawable)
    AsteroidFields.containers = (game.updatable)

    asteroid_field = AsteroidFields()

    Player.containers = (game.updatable, game.drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    loop(game, player)

def loop(game: GameCtrl, player: Player):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        
        game.updatable.update(game.dt)

        game.screen.fill((0,0,0))
        
        for entity in game.drawable:
            entity.draw(game.screen)

        pygame.display.flip()

        # limits the framerate to 60 FPS
        game.dt = game.clock.tick(60) / 1000


if __name__ == "__main__":
    main()