import pygame
from pygame.locals import *
from sys import exit
from settings import *

pygame.init()

tela = pygame.display.set_mode((WIDTH, HEIGHT))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.display.update()