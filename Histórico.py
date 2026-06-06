from player import Player

b = []
player = Player()

# LINHA 6: A função agora só precisa da lista e do objeto player
def adicionar_historico(lista_b, player_obj):
    # Puxa o 'dinheiro' do player para usar como saldo
    player_obj.cont_pontos(player_obj.dinheiro)

    # Monta o dicionário puxando os atributos de dentro do objeto (player_obj.atributo)
    a = {
        "aluguel": player_obj.aluguel,
        "comida": player_obj.comida,
        "remedio": player_obj.remedio,
        "saldo": player_obj.dinheiro,
        "pontos" : player_obj.pontos
    }
    lista_b.append(a)



