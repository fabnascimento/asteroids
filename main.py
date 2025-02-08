# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

class GameState(object):
    _instance = None
    name = ""

    def __init__(self):
        raise RuntimeError('Call instance() instead')
    
    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
            cls._instance.name = "Zamir"

        return cls._instance



def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    is_running = True
    _state = GameState.instance()

    loop(screen)

def loop(screen: pygame.Surface):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill((0,0,0))

        pygame.display.flip()


if __name__ == "__main__":
    main()