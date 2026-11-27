import pygame
import pygame
from pygame.locals import *
from sys import exit
from settings import *


largura = 1200
altura = 896

# CENAS E SEUS CAMINHOS 
tela_inicial = pygame.image.load("src/imagens/Tela_inicial.jpg")
tela_inicial = pygame.transform.scale(tela_inicial, (largura, altura))


pygame.init()
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Pelas Ruas Que Andei")
cena = "inicio"

# BOTÕES DA TELA INICIAL
botao_jogar = pygame.Rect(444, 394, 310, 124)
botao_sair = pygame.Rect(443, 537, 312, 122)
botao_creditos = pygame.Rect(953, 777, 199, 78)

game_ativo = True


def main():
    pygame.init()
    pygame.font.init()
  
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("WINDOW_TITLE")

    clock = pygame.time.Clock()
    while game_ativo:
        clock.tick(FPS)
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                game_ativo = False
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if cena == "inicio":
                    if botao_jogar.collidepoint(evento.pos):
                        cena == "primeira_fase"
                    elif botao_sair.collidepoint(evento.pos):
                        game_ativo = False
                    elif botao_creditos.collidepoint(evento.pos):
                        cena = "creditos"
        

        if cena == "inicio":
            janela.blit(tela_inicial, (0, 0))




    pygame.display.flip()