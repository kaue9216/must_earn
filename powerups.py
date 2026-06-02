from player import Player
import acoesv2

# 1. Instanciando o jogador
jogador = Player("Must Earn")

# Dicionário inicial (Valores Base fixos em 1.0)
dicionario_ativos = {
    "bigtech_cons": 1.0, "bigtech_int": 1.0, "bigtech_arr": 1.0,
    "fintech_cons": 1.0, "fintech_int": 1.0, "fintech_arr": 1.0,
    "cripto_cons": 1.0, "cripto_int": 1.0, "cripto_arr": 1.0
}

if jogador.dinheiro == 1500:
    jogador.aumentar_comida()
    jogador.aumentar_aluguel()
    jogador.aumentar_remdio()

    # 1️⃣ PASSO: Enviamos uma cópia para o mercado gerar as oscilações aleatórias
    dicionario_do_mercado, cenario_escolhido = acoesv2.aplicar_cenario(dicionario_ativos.copy())

    # 2️⃣ PASSO: Criamos OUTRA cópia para aplicar a sua inversão por -1 sem destruir o passo anterior
    dicionario_invertido = dicionario_do_mercado.copy()
    for chave in dicionario_invertido:
        dicionario_invertido[chave] = dicionario_invertido[chave] * -1

    # 📊 AUDITORIA COMPLETA NO TERMINAL
    print(f"\n🎬 Cenário Sorteado no acoesv2.py: Cenário {cenario_escolhido}")
    print("--------------------------------------------------")

    print("1) ANTES (Valores Base Iniciais):")
    print(dicionario_ativos)

    print("\n2) MEIO (Resultado Puro gerado pelo acoesv2.py):")
    print(dicionario_do_mercado)

    print("\n3) DEPOIS (Seu pseudocódigo aplicado: Individualmente por -1):")
    print(dicionario_invertido)
    print("--------------------------------------------------")


#---------------------------------------------------------------------------#
