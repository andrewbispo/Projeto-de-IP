import pygame

pygame.init()

cena_atual = "inicio"

game_ativo = True
while game_ativo:
    janela = pygame.display.set_mode((960, 640))
    pygame.display.set_caption("Pelas Ruas Que Andei")
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            game_ativo = False