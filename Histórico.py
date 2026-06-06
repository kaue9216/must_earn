# A lista fica guardada aqui, vazia no início do jogo
lista_historico = []

def registrar_dia(player_obj):
    # Atualiza os pontos puxando o dinheiro atual do objeto passado pela GUI
    player_obj.cont_pontos(player_obj.dinheiro)

    # Monta o dicionário
    a = {
        "aluguel": player_obj.aluguel,
        "comida": player_obj.comida,
        "remedio": player_obj.remedio,
        "saldo": player_obj.dinheiro,
        "pontos": player_obj.pontos
    }

    # Adiciona na lista
    lista_historico.append(a)

    # Imprime no terminal para você debugar e acompanhar
    print(f"Histórico atualizado: {lista_historico}")
