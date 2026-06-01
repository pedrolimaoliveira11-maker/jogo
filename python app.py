import pygame

pygame.init()

# Tela maior
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Jogo de Luta Completo")

clock = pygame.time.Clock()
FPS = 120

# Cores
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Lutadores
player1 = pygame.Rect(200, 500, 80, 120)
player2 = pygame.Rect(1000, 500, 80, 120)

# Vida inicial
vida1 = 100
vida2 = 100

# Fonte para mensagens
font = pygame.font.SysFont("Arial", 50)

running = True
winner = None

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # Movimento Player 1 (setas)
    if keys[pygame.K_LEFT]:
        player1.x -= 5
    if keys[pygame.K_RIGHT]:
        player1.x += 5
    if keys[pygame.K_UP]:
        player1.y -= 5
    if keys[pygame.K_DOWN]:
        player1.y += 5
    ataque1 = keys[pygame.K_SPACE]

    # Movimento Player 2 (WASD)
    if keys[pygame.K_a]:
        player2.x -= 5
    if keys[pygame.K_d]:
        player2.x += 5
    if keys[pygame.K_w]:
        player2.y -= 5
    if keys[pygame.K_s]:
        player2.y += 5
    ataque2 = keys[pygame.K_f]

    # Atualiza tela
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, player1)
    pygame.draw.rect(screen, BLUE, player2)

    # Ataque Player 1
    if ataque1 and vida2 > 0:
        golpe1 = pygame.Rect(player1.right, player1.y + 40, 30, 20)
        pygame.draw.rect(screen, BLACK, golpe1)
        if golpe1.colliderect(player2):
            vida2 -= 1

    # Ataque Player 2
    if ataque2 and vida1 > 0:
        golpe2 = pygame.Rect(player2.left - 30, player2.y + 40, 30, 20)
        pygame.draw.rect(screen, BLACK, golpe2)
        if golpe2.colliderect(player1):
            vida1 -= 1

    # Barras de vida
    pygame.draw.rect(screen, GREEN, (50, 50, vida1 * 3, 30))   # Player 1
    pygame.draw.rect(screen, GREEN, (800, 50, vida2 * 3, 30))  # Player 2

    # Condição de vitória
    if vida1 <= 0 and winner is None:
        winner = "Player 2 venceu!"
    elif vida2 <= 0 and winner is None:
        winner = "Player 1 venceu!"

    if winner:
        texto = font.render(winner, True, BLACK)
        screen.blit(texto, (400, 300))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
import pygame

pygame.init()

# Tela maior
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Jogo de Luta Completo")

clock = pygame.time.Clock()
FPS = 120

# Cores
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Lutadores
player1 = pygame.Rect(200, 500, 80, 120)
player2 = pygame.Rect(1000, 500, 80, 120)

# Vida inicial
vida1 = 100
vida2 = 100

# Fonte para mensagens
font = pygame.font.SysFont("Arial", 50)

running = True
winner = None

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # Movimento Player 1 (setas)
    if keys[pygame.K_LEFT]:
        player1.x -= 5
    if keys[pygame.K_RIGHT]:
        player1.x += 5
    if keys[pygame.K_UP]:
        player1.y -= 5
    if keys[pygame.K_DOWN]:
        player1.y += 5
    ataque1 = keys[pygame.K_SPACE]

    # Movimento Player 2 (WASD)
    if keys[pygame.K_a]:
        player2.x -= 5
    if keys[pygame.K_d]:
        player2.x += 5
    if keys[pygame.K_w]:
        player2.y -= 5
    if keys[pygame.K_s]:
        player2.y += 5
    ataque2 = keys[pygame.K_f]

    # Atualiza tela
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, player1)
    pygame.draw.rect(screen, BLUE, player2)

    # Ataque Player 1
    if ataque1 and vida2 > 0:
        golpe1 = pygame.Rect(player1.right, player1.y + 40, 30, 20)
        pygame.draw.rect(screen, BLACK, golpe1)
        if golpe1.colliderect(player2):
            vida2 -= 1

    # Ataque Player 2
    if ataque2 and vida1 > 0:
        golpe2 = pygame.Rect(player2.left - 30, player2.y + 40, 30, 20)
        pygame.draw.rect(screen, BLACK, golpe2)
        if golpe2.colliderect(player1):
            vida1 -= 1

    # Barras de vida
    pygame.draw.rect(screen, GREEN, (50, 50, vida1 * 3, 30))   # Player 1
    pygame.draw.rect(screen, GREEN, (800, 50, vida2 * 3, 30))  # Player 2

    # Condição de vitória
    if vida1 <= 0 and winner is None:
        winner = "Player 2 venceu!"
    elif vida2 <= 0 and winner is None:
        winner = "Player 1 venceu!"

    if winner:
        texto = font.render(winner, True, BLACK)
        screen.blit(texto, (400, 300))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
v
