# this allows us to use code
# from open-source pygame library
# throughout this file
import os, sys
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from constants import *
from player import *
from asteroidfield import *
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    
    
    updatable  = pygame.sprite.Group()
    drawable  = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers =(updatable)
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)
    player = Player(x, y)

    # game loop
    while True:
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                return
        

        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit()
        
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                    shot.kill()
                    asteroid.split()

        screen.fill(color="black")

        for obj in drawable:
            obj.draw(screen)

        
        pygame.display.flip()
        # limit the framerate to 60 fps
        dt = clock.tick(60) / 1000
        


    




if __name__ == "__main__":
    main()
