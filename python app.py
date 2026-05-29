import pygame
import random
import sys

# Inicializa o Pygame
pygame.init()

# Configurações da tela
largura, altura = 600, 400
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo com Imagens de Derrota")

# Cores
BRANCO = (255, 255, 255)
VERMELHO = (200, 0, 0)
VERDE = (0, 200, 0)

# Fonte
fonte = pygame.font.SysFont("Arial", 36)

# Carregar imagens dos jogadores
img_jogador1 = pygame.image.load("jogador1.png")  # coloque a imagem na mesma pasta
img_jogador2 = pygame.image.load("jogador2.png")

def mostrar_mensagem(texto, cor, imagem=None):
    tela.fill(BRANCO)
    mensagem = fonte.render(texto, True, cor)
    rect = mensagem.get_rect(center=(largura//2, altura//2 - 50))
    tela.blit(mensagem, rect)

    if imagem:
        img_rect = imagem.get_rect(center=(largura//2, altura//2 + 80))
        tela.blit(imagem, img_rect)

    pygame.display.update()
    pygame.time.delay(2000)

def jogo():
    jogadores = ["Jogador 1", "Jogador 2"]
    vencedor = random.choice(jogadores)
    perdedor = [j for j in jogadores if j != vencedor][0]

    if vencedor == "Jogador 1":
        mostrar_mensagem(f"O vencedor é {vencedor}! 🎉", VERDE, img_jogador1)
        mostrar_mensagem(f"{perdedor} foi derrotado! 😢", VERMELHO, img_jogador2)
    else:
        mostrar_mensagem(f"O vencedor é {vencedor}! 🎉", VERDE, img_jogador2)
        mostrar_mensagem(f"{perdedor} foi derrotado! 😢", VERMELHO, img_jogador1)

# Loop principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if evento.type == pygame.KEYDOWN:  # Pressione qualquer tecla para jogar
            jogo()
