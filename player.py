import pygame
from constants import *
from circleshape import CircleShape
from asteroidfield import AsteroidField
from shot import Shoot

class Player(CircleShape):
    #call parent, and pass Player_Radius
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)

        self.rotation = 0
        self.timer = 0
    
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self,screen):
        color = (255,255,255)
        pygame.draw.polygon(screen,color,self.triangle(),2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()
        #rotate with key press
        if keys[pygame.K_a]:
            self.rotate(dt*-1)
        if keys[pygame.K_d]:
            self.rotate(dt)
        #move the player
        if keys[pygame.K_s]:
            self.move(dt*-1)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
        

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    
    def shoot(self):
        if self.timer <= 0:
            bullet = Shoot(self.position.x, self.position.y)
            bullet.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
            self.timer = PLAYER_SHOOT_COOLDOWN
