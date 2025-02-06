from circleshape import CircleShape
import pygame

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

# draw override to create filled in circles
    def draw(self, screen):
        return pygame.draw.circle(screen, "white", self.position, self.radius, 2)

# update override to move asteroid objects
    def update(self, dt):
        self.position += self.velocity * dt
