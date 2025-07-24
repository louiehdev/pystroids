import pygame
import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "White", self.position, self.radius, 2)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            split_asteroid_one = Asteroid(self.position.x, self.position.y, new_radius)
            split_asteroid_two = Asteroid(self.position.x, self.position.y, new_radius)
            split_asteroid_one.velocity = self.velocity.rotate(random_angle) * 1.2
            split_asteroid_two.velocity = self.velocity.rotate(-random_angle)
    
    def update(self, dt):
        self.position += self.velocity * dt
