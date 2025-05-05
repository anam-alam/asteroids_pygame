# this allows us to use code
# from open-source pygame library
# throughout this file
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from constants import *
from player import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    
    
    updatable  = pygame.sprite.Group()
    drawable  = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(x, y)

    # game loop
    while True:
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                return
        

        updatable.update(dt)
        
        screen.fill(color="black")
        
        for obj in drawable:
            obj.draw(screen)

        
        pygame.display.flip()
        # limit the framerate to 60 fps
        dt = clock.tick(60) / 1000
        


    




if __name__ == "__main__":
    main()
