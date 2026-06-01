import pygame

# Inicializa o Pygame
pygame.init()

# Aumenta o tamanho da tela (gráfico maior)
screen = pygame.display.set_mode((1280, 720))  # resolução maior
pygame.display.set_caption("Meu Jogo de Luta")

# Controlador de FPS
clock = pygame.time.Clock()
FPS = 120  # aumenta FPS (padrão seria 60)

# Cores
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Personagem (um quadrado simples)
player = pygame.Rect(100, 500, 80, 120)  # posição x,y e tamanho

# Loop principal
running = True
while running:
    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movimento básico
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= 5
    if keys[pygame.K_RIGHT]:
        player.x += 5

    # Atualiza tela
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, player)  # desenha personagem
    pygame.display.flip()

    # Controla FPS
    clock.tick(FPS)

pygame.quit()
