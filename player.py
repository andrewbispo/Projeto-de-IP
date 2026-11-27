import pygame
from settings import *

class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 28, 28)

        self.speed = PLAYER_SPEED
        self.lives = PLAYER_LIVES

        self.boost_active = False
        self.boost_end = 0

        self.invulnerable_until = 0

    def move(self, keys, walls):
        dx = 0
        dy = 0

        if keys[pygame.K_w]:
            dy = -self.speed

        if keys[pygame.K_s]:
            dy = self.speed

        if keys[pygame.K_a]:
            dx = -self.speed

        if keys[pygame.K_d]:
            dx = self.speed