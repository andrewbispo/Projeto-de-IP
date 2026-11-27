import pygame
from settings import *

class Enemy:

    def __init__(self, x, y, behavior="patrol"):

        self.rect = pygame.Rect(x, y, 28, 28)
        self.speed = ENEMY_SPEED
        self.behavior = behavior
        self.direction = 1

    def move_with_collision(self, dx, dy, walls):

        self.rect.x += dx

        for wall in walls:
            if self.rect.colliderect(wall):
                if dx > 0:
                    self.rect.right = wall.left
                elif dx < 0:
                    self.rect.left = wall.right

        self.rect.y += dy

        for wall in walls:
            if self.rect.colliderect(wall):
                if dy > 0:
                    self.rect.bottom = wall.top
                elif dy < 0:
                    self.rect.top = wall.bottom

    def chase_player(self, player, walls):

        dx = player.rect.centerx - self.rect.centerx
        dy = player.rect.centery - self.rect.centery

        if abs(dx) > abs(dy):
            mx = self.speed if dx > 0 else -self.speed
            my = 0
        else:
            mx = 0
            my = self.speed if dy > 0 else -self.speed

        self.move_with_collision(mx, my, walls)

    def patrol(self, walls):

        old_x = self.rect.x

        self.move_with_collision(
            self.speed * self.direction,
            0,
            walls
        )

        if self.rect.x == old_x:
            self.direction *= -1

    def update(self, player, walls):
        if self.behavior == "chase":
            self.chase_player(player, walls)
        elif self.behavior == "patrol":
            self.patrol(walls)

    def draw(self, screen):
        color = (220, 50, 50)

        if self.behavior == "patrol":
            color = (180, 70, 220)

        pygame.draw.rect(screen, color, self.rect, border_radius=8)