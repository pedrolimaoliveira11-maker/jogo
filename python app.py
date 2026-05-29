import pygame
import random
import sys

# Inicializa o Pygame
pygame.init()

# Configurações da tela
largura, altura = 800, 500
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo Realista de Vitória e Derrota")

# Cores
BRANCO = (255, 255, 255)
VERDE = (0, 200, 0)
VERMELHO = (200, 0, 0)
PRETO = (0, 0, 0)

# Fonte
fonte = pygame.font.SysFont("Arial", 36)

# Sons
som_vitoria = pygame.mixer.Sound("vitoria.wav")
som_derrota = pygame.mixer.Sound("derrota.wav")

# Imagens
img_jogador1 = pygame.image.load("jogador1.png")
img_jogador2 = pygame.image.load("jogador2.png")

# Pontuação
pontuacao = {"Jogador 1": 0, "Jogador 2": 0}

def animar_personagem(imagem, pos_inicial, pos_final, duracao):
    x, y = pos_inicial
    dx = (pos_final[0] - x) / duracao
    dy = (pos_final[1] - y) / duracao
    for i in range(duracao):
        tela.fill(BRANCO)
        tela.blit(imagem, (x + dx*i, y + dy*i))
        pygame.display.update()
        pygame.time.delay(20)

def efeito_explosao(cor):
    for i in range(50):
        x = random.randint(0, largura)
        y = random.randint(0, altura)
        pygame.draw.circle(tela, cor, (x, y), random.randint(2, 6))
    pygame.display.update()
    pygame.time.delay(500)

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

def atualizar_pontuacao(vencedor):
    pontuacao[vencedor] += 1

def tela_resultado():
    tela.fill(BRANCO)
    texto = fonte.render(f"Placar: Jogador 1 - {pontuacao['Jogador 1']} | Jogador 2 - {pontuacao['Jogador 2']}", True, PRETO)
    rect = texto.get_rect(center=(largura//2, altura//2))
    tela.blit(texto, rect)
    pygame.display.update()
    pygame.time.delay(2500)

def jogo():
    jogadores = ["Jogador 1", "Jogador 2"]
    vencedor = random.choice(jogadores)
    perdedor = [j for j in jogadores if j != vencedor][0]

    if vencedor == "Jogador 1":
        som_vitoria.play()
        animar_personagem(img_jogador1, (100, 300), (400, 200), 30)
        efeito_explosao(VERDE)
        mostrar_mensagem(f"{vencedor} venceu! 🎉", VERDE, img_jogador1)
        som_derrota.play()
        mostrar_mensagem(f"{perdedor} perdeu! 😢", VERMELHO, img_jogador2)
    else:
        som_vitoria.play()
        animar_personagem(img_jogador2, (600, 300), (400, 200), 30)
        efeito_explosao(VERDE)
        mostrar_mensagem(f"{vencedor} venceu! 🎉", VERDE, img_jogador2)
        som_derrota.play()
        mostrar_mensagem(f"{perdedor} perdeu! 😢", VERMELHO, img_jogador1)

    atualizar_pontuacao(vencedor)
    tela_resultado()

# Loop principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == pygame.KEYDOWN:
            jogo()
