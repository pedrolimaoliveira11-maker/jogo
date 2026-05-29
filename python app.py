from ursina import *
import random

app = Ursina()

# Criar jogadores como cubos 3D
jogador1 = Entity(model='cube', color=color.azure, position=(-2,0,0))
jogador2 = Entity(model='cube', color=color.red, position=(2,0,0))

texto = Text(text='', origin=(0,0), scale=2, y=0.3)

def jogo():
    vencedor = random.choice(["Jogador 1", "Jogador 2"])
    perdedor = "Jogador 1" if vencedor == "Jogador 2" else "Jogador 2"

    if vencedor == "Jogador 1":
        jogador1.color = color.green
        jogador2.color = color.red
    else:
        jogador2.color = color.green
        jogador1.color = color.red

    texto.text = f"{vencedor} venceu! {perdedor} perdeu!"

def input(key):
    if key == 'space':  # Pressione espaço para jogar
        jogo()

app.run()
