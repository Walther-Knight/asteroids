import pygame
from constants import *
import player



def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fps_clock = pygame.time.Clock()
    dt = 0
    player_ship = player.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
          for event in pygame.event.get():
                if event.type == pygame.QUIT:
                      return
          screen.fill("black")
          player_ship.update(dt)
          player_ship.draw(screen)
          pygame.display.flip()
          dt = fps_clock.tick(60) / 1000      
    #print("Starting asteroids!")
    #print(f"Screen width: {SCREEN_WIDTH}")
    #print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
        main()