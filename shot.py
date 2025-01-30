import pygame
from circleshape import CircleShape
from constants import *

class Shoot(CircleShape):
    def __init__(self, x, y):
       super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        color = "white"
        pygame.draw.circle(screen, color, self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt