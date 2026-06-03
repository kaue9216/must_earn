import acoesv2 as acoes
from player import Player

player = Player()
player.aumemtar_max_aluguel(1)
player.aumentar_max_comida(1)
player.aumentar_max_remedio(1)

print(acoes.aplicar_cenario)


def macaco_digital():
    player.adicionar_dinheiro(-50000)
    print(player.dinheiro)

macaco_digital()
