import pygame

largura = 1200
altura = 896
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

while game_ativo:

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            game_ativo = False
        if evento.type == pygame.MOUSEBUTTONDOWN:
            print(evento.pos)
    

    if cena == "inicio":
        janela.blit(tela_inicial, (0, 0))
        pygame.display.flip()