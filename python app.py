from ursina import *

app = Ursina()

# Criar jogadores como cubos 3D
jogador1 = Entity(model='cube', color=color.azure, position=(-2,0,0))
jogador2 = Entity(model='cube', color=color.red, position=(2,0,0))

# Vida inicial
vida_jogador1 = 20
vida_jogador2 = 20

# Texto na tela
texto = Text(text='', origin=(0,0), scale=2, y=0.3)

# Barras de vida
barra1 = Entity(model='quad', color=color.green, scale=(0.4,0.05), position=(-0.5,0.4))
barra2 = Entity(model='quad', color=color.green, scale=(0.4,0.05), position=(0.5,0.4))

def atualizar_barras():
    barra1.scale_x = vida_jogador1 / 20 * 0.4
    barra2.scale_x = vida_jogador2 / 20 * 0.4

def aplicar_dano(jogador, dano):
    global vida_jogador1, vida_jogador2
    if jogador == "Jogador 1":
        vida_jogador1 -= dano
        texto.text = f"Jogador 1 tomou {dano} de dano!"
    else:
        vida_jogador2 -= dano
        texto.text = f"Jogador 2 tomou {dano} de dano!"
    atualizar_barras()

def input(key):
    global vida_jogador1, vida_jogador2
    if key == '1':  # Jogador 1 leva soco
        aplicar_dano("Jogador 1", 6)
    if key == '2':  # Jogador 2 leva soco
        aplicar_dano("Jogador 2", 6)

    # Verifica se alguém perdeu
    if vida_jogador1 <= 0:
        texto.text = "Jogador 1 foi derrotado!"
    if vida_jogador2 <= 0:
        texto.text = "Jogador 2 foi derrotado!"

app.run()
