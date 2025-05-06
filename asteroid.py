from circleshape import CircleShape
import pygame
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle  = random.uniform(20.0, 50.0)
        v1 = self.velocity.rotate(random_angle)
        v2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        small_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        small_asteroid_1.velocity = v1*1.2
        small_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        small_asteroid_2.velocity = v2*1.2
        