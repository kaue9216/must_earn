def validar_nome_disponivel(nome: str):
    with open("./jogadores.txt", "r", encoding="utf-8") as jogadores:
        conteudo_jogadores = jogadores.readlines()

    
    if not conteudo_jogadores:
        return True


    for linha in conteudo_jogadores:
        linha = linha.strip()
        if not linha:
            continue
        if len(linha.split("/")) != 4:
            continue
        username, n_rodadas, lucro_total, ganhou = linha.split("/")

        if username == nome:
            return False
    return True
    

def gerar_relatorio(player_username, player_rodadas, player_lucro_total, player_ganhou):
    with open("./jogadores.txt", "a", encoding="utf-8") as jogadores:
        if player_ganhou:
            player_ganhou = "Ganhou"
        else:
            player_ganhou = "Perdeu"
        jogadores.write(f"\n{player_username}/{player_rodadas}/{player_lucro_total}/{player_ganhou}\n")

    with open("./jogadores.txt", "r", encoding="utf-8") as jogadores:
        conteudo_jogadores = jogadores.readlines()
        print(conteudo_jogadores)


    jogadores = []

    vencedores = []
    perdedores = []


    for linha in conteudo_jogadores:
        linha = linha.strip()
        if not linha:
            continue
        if len(linha.split("/")) != 4:
            continue
        username, n_rodadas, lucro_total, ganhou = linha.split("/")
        jogadores.append((username, n_rodadas, lucro_total, ganhou))


    for jogador in jogadores:
        if jogador[3] == "Ganhou":
            vencedores.append(jogador)
        else:
            perdedores.append(jogador)


    vencedores.sort(key=lambda x: x[1])
    perdedores.sort(key=lambda x: x[1], reverse=True)


    with open("./relatorio.txt", "w", encoding="utf-8") as relatorio:
        relatorio.write("--- VENCEDORES ---\n")
        ranking_vencedores = 1
        for v in vencedores:
            relatorio.write(f"\n{ranking_vencedores}º - {v[0]}:\n-Rodadas: {v[1]}\n-Lucro Total: R${float(v[2]):.2f}\n-{v[3]}\n")
            ranking_vencedores += 1
        
        relatorio.write("\n--- PERDEDORES ---\n")
        ranking_perdedores = 1
        for p in perdedores:
            relatorio.write(f"\n{ranking_perdedores}º - {p[0]}:\n-Rodadas: {p[1]}\n-Lucro Total: R${float(p[2]):.2f}\n-{p[3]}\n")
            ranking_perdedores += 1