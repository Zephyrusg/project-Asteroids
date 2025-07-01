import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,2)
    
    def update(self,dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20,50)
        NewAsteroids = []
        NewAsteroids.append(self.velocity.rotate(-angle))
        NewAsteroids.append(self.velocity.rotate(angle))

        radius = self.radius - ASTEROID_MIN_RADIUS
        for asteroid in NewAsteroids:
            newandroid =Asteroid(self.position.x, self.position.y,radius)
            newandroid.velocity += asteroid * 1.2
