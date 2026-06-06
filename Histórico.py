from player import Player

b =[]
player = Player()

def adicionar_historico(aluguel, comida, remedio, saldo, lista_b, player):
    player.cont_pontos(saldo)
    a = {"aluguel":aluguel, "comida":comida, "remedio": remedio, "saldo":saldo, "pontos": player.pontos}
    lista_b.append(a)

aluguel = 1
comida = 1
remedio = 1
saldo = 1
teste = 0
while teste < 5:
    adicionar_historico(aluguel, comida, remedio, saldo, b, player)
    teste = teste+1

for x in b:
    print(x)

print(b)
print(f"Pontuação total do jogador: {player.pontos}")
