# acoesv2.py
import random
import textos  # Conectando com o seu arquivo de textos

def aplicar_cenario(cenario, dicionario):
    # Cenário 1: Ações bigtech crescem, ações fintech permanecem estáveis e ações cripto caem
    if cenario == 1:
        # Bigtech: Cresce
        dicionario["bigtech_cons"] *= random.randint(-10, 20) / 100
        dicionario["bigtech_int"] *= random.randint(-20, 40) / 100
        dicionario["bigtech_arr"] *= random.randint(-50, 100) / 100

        # Fintech: Estável
        dicionario["fintech_cons"] *= random.randint(-15, 15) / 100
        dicionario["fintech_int"] *= random.randint(-30, 30) / 100
        dicionario["fintech_arr"] *= random.randint(-75, 75) / 100

        # Cripto: Queda
        dicionario["cripto_cons"] *= random.randint(-20, 10) / 100
        dicionario["cripto_int"] *= random.randint(-40, 20) / 100
        dicionario["cripto_arr"] *= random.randint(-100, 50) / 100

    # Cenário 2: Ações bigtech permanecem estáveis, ações fintech caem e ações cripto crescem
    elif cenario == 2:
        # Bigtech: Estável
        dicionario["bigtech_cons"] *= random.randint(-15, 15) / 100
        dicionario["bigtech_int"] *= random.randint(-30, 30) / 100
        dicionario["bigtech_arr"] *= random.randint(-75, 75) / 100

        # Fintech: Queda
        dicionario["fintech_cons"] *= random.randint(-20, 10) / 100
        dicionario["fintech_int"] *= random.randint(-40, 20) / 100
        dicionario["fintech_arr"] *= random.randint(-100, 50) / 100

        # Cripto: Cresce
        dicionario["cripto_cons"] *= random.randint(-10, 20) / 100
        dicionario["cripto_int"] *= random.randint(-20, 40) / 100
        dicionario["cripto_arr"] *= random.randint(-50, 100) / 100

    # Cenário 3: Ações bigtech caem, ações fintech crescem e ações cripto permanecem estáveis
    elif cenario == 3:
        # Bigtech: Queda
        dicionario["bigtech_cons"] *= random.randint(-20, 10) / 100
        dicionario["bigtech_int"] *= random.randint(-40, 20) / 100
        dicionario["bigtech_arr"] *= random.randint(-100, 50) / 100

        # Fintech: Cresce
        dicionario["fintech_cons"] *= random.randint(-10, 20) / 100
        dicionario["fintech_int"] *= random.randint(-20, 40) / 100
        dicionario["fintech_arr"] *= random.randint(-50, 100) / 100

        # Cripto: Estável
        dicionario["cripto_cons"] *= random.randint(-15, 15) / 100
        dicionario["cripto_int"] *= random.randint(-30, 30) / 100
        dicionario["cripto_arr"] *= random.randint(-75, 75) / 100

    # Cenário 4: Ações bigtech crescem, ações fintech crescem e ações cripto caem
    elif cenario == 4:
        # Bigtech: Cresce
        dicionario["bigtech_cons"] *= random.randint(-10, 20) / 100
        dicionario["bigtech_int"] *= random.randint(-20, 40) / 100
        dicionario["bigtech_arr"] *= random.randint(-50, 100) / 100

        # Fintech: Cresce
        dicionario["fintech_cons"] *= random.randint(-10, 20) / 100
        dicionario["fintech_int"] *= random.randint(-20, 40) / 100
        dicionario["fintech_arr"] *= random.randint(-50, 100) / 100

        # Cripto: Queda
        dicionario["cripto_cons"] *= random.randint(-20, 10) / 100
        dicionario["cripto_int"] *= random.randint(-40, 20) / 100
        dicionario["cripto_arr"] *= random.randint(-100, 50) / 100

    # Cenário 5: Ações bigtech crescem, ações fintech caem e ações cripto crescem
    elif cenario == 5:
        # Bigtech: Cresce
        dicionario["bigtech_cons"] *= random.randint(-10, 20) / 100
        dicionario["bigtech_int"] *= random.randint(-20, 40) / 100
        dicionario["bigtech_arr"] *= random.randint(-50, 100) / 100

        # Fintech: Queda
        dicionario["fintech_cons"] *= random.randint(-20, 10) / 100
        dicionario["fintech_int"] *= random.randint(-40, 20) / 100
        dicionario["fintech_arr"] *= random.randint(-100, 50) / 100

        # Cripto: Cresce
        dicionario["cripto_cons"] *= random.randint(-10, 20) / 100
        dicionario["cripto_int"] *= random.randint(-20, 40) / 100
        dicionario["cripto_arr"] *= random.randint(-50, 100) / 100

    # Cenário 6: Ações bigtech caem, ações fintech crescem e ações cripto crescem
    elif cenario == 6:
        # Bigtech: Queda
        dicionario["bigtech_cons"] *= random.randint(-20, 10) / 100
        dicionario["bigtech_int"] *= random.randint(-40, 20) / 100
        dicionario["bigtech_arr"] *= random.randint(-100, 50) / 100

        # Fintech: Cresce
        dicionario["fintech_cons"] *= random.randint(-10, 20) / 100
        dicionario["fintech_int"] *= random.randint(-20, 40) / 100
        dicionario["fintech_arr"] *= random.randint(-50, 100) / 100

        # Cripto: Cresce
        dicionario["cripto_cons"] *= random.randint(-10, 20) / 100
        dicionario["cripto_int"] *= random.randint(-20, 40) / 100
        dicionario["cripto_arr"] *= random.randint(-50, 100) / 100

    # Cenário 7: Todas as ações crescem
    elif cenario == 7:
        # Bigtech: Cresce
        dicionario["bigtech_cons"] *= random.randint(-10, 20) / 100
        dicionario["bigtech_int"] *= random.randint(-20, 40) / 100
        dicionario["bigtech_arr"] *= random.randint(-50, 100) / 100

        # Fintech: Cresce
        dicionario["fintech_cons"] *= random.randint(-10, 20) / 100
        dicionario["fintech_int"] *= random.randint(-20, 40) / 100
        dicionario["fintech_arr"] *= random.randint(-50, 100) / 100

        # Cripto: Cresce
        dicionario["cripto_cons"] *= random.randint(-10, 20) / 100
        dicionario["cripto_int"] *= random.randint(-20, 40) / 100
        dicionario["cripto_arr"] *= random.randint(-50, 100) / 100

    # Cenário 8: Todas as ações caem
    elif cenario == 8:
        # Bigtech: Queda
        dicionario["bigtech_cons"] *= random.randint(-20, 10) / 100
        dicionario["bigtech_int"] *= random.randint(-40, 20) / 100
        dicionario["bigtech_arr"] *= random.randint(-100, 50) / 100

        # Fintech: Queda
        dicionario["fintech_cons"] *= random.randint(-20, 10) / 100
        dicionario["fintech_int"] *= random.randint(-40, 20) / 100
        dicionario["fintech_arr"] *= random.randint(-100, 50) / 100

        # Cripto: Queda
        dicionario["cripto_cons"] *= random.randint(-20, 10) / 100
        dicionario["cripto_int"] *= random.randint(-40, 20) / 100
        dicionario["cripto_arr"] *= random.randint(-100, 50) / 100

    return dicionario


# --- Inicialização dos Dados ---
dicionario_ativos = {
    "bigtech_cons" : 1, "bigtech_int" : 1, "bigtech_arr" : 1,
    "fintech_cons" : 1, "fintech_int" : 1, "fintech_arr" : 1,
    "cripto_cons" : 1, "cripto_int" : 1, "cripto_arr" : 1
}

lista = [1, 2, 3, 4, 5, 6, 7, 8]
escolha_cenario = random.randint(0, 7)
cenario_sorteado = lista[escolha_cenario]


# --- Processamento ---
# 1. Aplica o cálculo matemático no dicionário
dicionario_atualizado = aplicar_cenario(cenario_sorteado, dicionario_ativos)

# 2. Puxa o texto correspondente do arquivo textos.py usando o id do cenário
texto_do_cenario = textos.cenarios.get(cenario_sorteado)


# --- Outputs Formatados no Terminal ---
print("=" * 60)
print("LORE DO MERCADO:")
print("=" * 60)
print(textos.lore)
print("\n" + "=" * 60)
print(f"NOTÍCIA DO CENÁRIO SORTEADO (Cenário {cenario_sorteado}):")
print("=" * 60)
print(texto_do_cenario)
print("\n" + "=" * 60)
print("VALOR ATUALIZADO DOS ATIVOS POST-PREGÃO:")
print("=" * 60)
for ativo, valor in dicionario_atualizado.items():
    print(f"{ativo}: {valor:.4f}")
print("=" * 60)
