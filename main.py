import pygame
from constants import *
from player import Player



def main():
    # call and configure pygame and set up fps
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # define pygame containers
    #updatable = pygame.sprite.Group()
    #drawable = pygame.sprite.Group()
    #Player.containers = (updatable, drawable)

    # define player_ship object
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)


    # game loop
    while True:
          for event in pygame.event.get():
                if event.type == pygame.QUIT:
                      return
          screen.fill("black")
          player.update(dt)
          player.draw(screen)
          pygame.display.flip()
          dt = clock.tick(60) / 1000      
    #print("Starting asteroids!")
    #print(f"Screen width: {SCREEN_WIDTH}")
    #print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
        main()