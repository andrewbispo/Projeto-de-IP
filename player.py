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

        # Movimento horizontal
        self.rect.x += dx

        for wall in walls:
            if self.rect.colliderect(wall):
                if dx > 0:
                    self.rect.right = wall.left
                elif dx < 0:
                    self.rect.left = wall.right

        # Movimento vertical
        self.rect.y += dy

        for wall in walls:
            if self.rect.colliderect(wall):
                if dy > 0:
                    self.rect.bottom = wall.top
                elif dy < 0:
                    self.rect.top = wall.bottom

    def activate_boost(self):
        self.speed = BOOST_SPEED
        self.boost_active = True
        self.boost_end = pygame.time.get_ticks() + BOOST_DURATION

    def update(self):
        now = pygame.time.get_ticks()

        if self.boost_active and now >= self.boost_end:
            self.speed = PLAYER_SPEED
            self.boost_active = False

    def take_damage(self):
        now = pygame.time.get_ticks()

        if now < self.invulnerable_until:
            return

        self.lives -= 1
        self.invulnerable_until = now + 1500

    def draw(self, screen):

        now = pygame.time.get_ticks()

        # Piscar durante a invulnerabilidade
        if now < self.invulnerable_until:
            if now // 150 % 2 == 0:
                return

        pygame.draw.rect(screen, (70, 160, 255), self.rect, border_radius=8)