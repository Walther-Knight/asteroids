from constants import *
from circleshape import CircleShape
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

# draw override to create filled in circles
    def draw(self, screen):
        return pygame.draw.circle(screen, "white", self.position, self.radius, 2)

# update override to move asteroid objects
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        

        angle = random.uniform(20, 50)

        vector1 = self.velocity.rotate(angle)
        vector2 = self.velocity.rotate(-angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = vector1 * 1.2
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = vector2 * 1.2
