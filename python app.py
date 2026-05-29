import pygame
import sys

# Inicializa o Pygame
pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Kickboxing Arena")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
BLUE = (0, 0, 200)
GREEN = (0, 200, 0)

# Relógio
clock = pygame.time.Clock()

# Classe do Lutador
class Fighter:
    def __init__(self, x, y, color, controls):
        self.rect = pygame.Rect(x, y, 50, 100)
        self.color = color
        self.health = 100
        self.controls = controls
        self.speed = 5
        self.attack_cooldown = 0

    def move(self, keys):
        if keys[self.controls["left"]]:
            self.rect.x -= self.speed
        if keys[self.controls["right"]]:
            self.rect.x += self.speed
        if keys[self.controls["up"]]:
            self.rect.y -= self.speed
        if keys[self.controls["down"]]:
            self.rect.y += self.speed

    def attack(self, opponent):
        if self.attack_cooldown == 0:
            attack_rect = pygame.Rect(self.rect.x - 10, self.rect.y, self.rect.width + 20, self.rect.height)
            if attack_rect.colliderect(opponent.rect):
                opponent.health -= 10
            self.attack_cooldown = 30

    def update(self):
        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        # Barra de vida
        pygame.draw.rect(surface, RED, (self.rect.x, self.rect.y - 20, 50, 10))
        pygame.draw.rect(surface, GREEN, (self.rect.x, self.rect.y - 20, 50 * (self.health / 100), 10))

# Controles dos jogadores
controls1 = {"left": pygame.K_a, "right": pygame.K_d, "up": pygame.K_w, "down": pygame.K_s, "attack": pygame.K_SPACE}
controls2 = {"left": pygame.K_LEFT, "right": pygame.K_RIGHT, "up": pygame.K_UP, "down": pygame.K_DOWN, "attack": pygame.K_RETURN}

# Criação dos lutadores
fighter1 = Fighter(200, 400, BLUE, controls1)
fighter2 = Fighter(550, 400, RED, controls2)

# Loop principal
running = True
while running:
    screen.fill(WHITE)

    # Arena
    pygame.draw.rect(screen, BLACK, (50, 500, 700, 50))  # chão

    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    fighter1.move(keys)
    fighter2.move(keys)

    if keys[controls1["attack"]]:
        fighter1.attack(fighter2)
    if keys[controls2["attack"]]:
        fighter2.attack(fighter1)

    fighter1.update()
    fighter2.update()

    fighter1.draw(screen)
    fighter2.draw(screen)

    # Verifica fim de jogo
    if fighter1.health <= 0 or fighter2.health <= 0:
        font = pygame.font.SysFont(None, 74)
        if fighter1.health <= 0:
            text = font.render("Jogador 2 Venceu!", True, BLACK)
        else:
            text = font.render("Jogador 1 Venceu!", True, BLACK)
        screen.blit(text, (200, 250))
        pygame.display.flip()
        pygame.time.wait(3000)
        running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
