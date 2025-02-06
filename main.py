import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fps_clock = pygame.time.Clock()
    dt = 0

    # create pygame sprite groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    # instantiate player object
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
# update updateable objects
        updatable.update(dt)

# player to asteroid collision check
        for asteroid in asteroids:
             if asteroid.collision(player):
                  print("Game over!")
                  sys.exit()

# shot to asteroid collision check
        for asteroid in asteroids:
             for shot in shots:
                  if asteroid.collision(shot):
                       asteroid.split()
                       shot.kill()

        screen.fill("black")
#iterate all drawable objects and draw them
        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()
# limit frame rate to 60 fps
        dt = fps_clock.tick(60) / 1000      
    #print("Starting asteroids!")
    #print(f"Screen width: {SCREEN_WIDTH}")
    #print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
        main()