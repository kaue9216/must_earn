import random
import numpy as np

def carteira_conservadora(carteira, inv_conservadores):
    for j in range(len(inv_conservadores)):
        dado_atual = inv_conservadores[j]
        if dado_atual == "":
            dado_atual = 0.0
        else:
            dado_atual = float(dado_atual)

        numero_randomico = random.randint(-20, 50) / 100
        carteira[0][j] = dado_atual * numero_randomico

    return carteira

def carteira_moderada(carteira, inv_intermediarios):
    for j in range(len(inv_intermediarios)):
        dado_atual = inv_intermediarios[j]
        if dado_atual == "":
            dado_atual = 0.0
        else:
            dado_atual = float(dado_atual)

        numero_randomico = random.randint(-50, 75) / 100
        carteira[1][j] = dado_atual * numero_randomico

    return carteira

def carteira_arrojada(carteira, inv_arrojados):
    for j in range(len(inv_arrojados)):
        dado_atual = inv_arrojados[j]
        if dado_atual == "":
            dado_atual = 0.0
        else:
            dado_atual = float(dado_atual)

        numero_randomico = random.randint(-100, 150) / 100
        carteira[2][j] = dado_atual * numero_randomico

    return carteira

carteira = np.zeros((3,3))

inv_conservadores = []
for j in range(3):
    entrada = input(f"Digite o valor para a posição [0][{j}] (ou Enter para 0): ").strip()
    inv_conservadores.append(entrada)

carteira = carteira_conservadora(carteira, inv_conservadores)

inv_intermediarios = []
for j in range(3):
    entrada = input(f"Digite o valor para a posição [1][{j}] (ou Enter para 0): ").strip()
    inv_intermediarios.append(entrada)

carteira = carteira_moderada(carteira, inv_intermediarios)

inv_arrojados = []
for j in range(3):
    entrada = input(f"Digite o valor para a posição [2][{j}] (ou Enter para 0): ").strip()
    inv_arrojados.append(entrada)

carteira = carteira_arrojada(carteira, inv_arrojados)

print(carteira)
