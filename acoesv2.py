# acoesv2.py
import random
import textos  # Conectando com o seu arquivo de textos

def aplicar_cenario(cenario, dicionario):
    # Cenário 1: Bigtech crescem, fintech estáveis e cripto caem
    if cenario == 1:
        dicionario["bigtech_cons"] *= random.randint(0, 50) / 100
        dicionario["bigtech_int"] *= random.randint(-5, 75) / 100
        dicionario["bigtech_arr"] *= random.randint(-10, 150) / 100

        dicionario["fintech_cons"] *= random.randint(0, 10) / 100
        dicionario["fintech_int"] *= random.randint(-10, 50) / 100
        dicionario["fintech_arr"] *= random.randint(-15, 75) / 100

        dicionario["cripto_cons"] *= random.randint(-10, 5) / 100
        dicionario["cripto_int"] *= random.randint(-15, 10) / 100
        dicionario["cripto_arr"] *= random.randint(-50, 15) / 100

    # Cenário 2: Bigtech estáveis, fintech caem e cripto crescem
    elif cenario == 2:
        dicionario["bigtech_cons"] *= random.randint(0, 10) / 100
        dicionario["bigtech_int"] *= random.randint(-10, 50) / 100
        dicionario["bigtech_arr"] *= random.randint(-15, 75) / 100

        dicionario["fintech_cons"] *= random.randint(-10, 5) / 100
        dicionario["fintech_int"] *= random.randint(-15, 10) / 100
        dicionario["fintech_arr"] *= random.randint(-50, 15) / 100

        dicionario["cripto_cons"] *= random.randint(0, 50) / 100
        dicionario["cripto_int"] *= random.randint(-5, 75) / 100
        dicionario["cripto_arr"] *= random.randint(-10, 150) / 100

    # Cenário 3: Bigtech caem, fintech crescem e cripto estáveis
    elif cenario == 3:
        dicionario["bigtech_cons"] *= random.randint(-10, 5) / 100
        dicionario["bigtech_int"] *= random.randint(-15, 10) / 100
        dicionario["bigtech_arr"] *= random.randint(-50, 15) / 100

        dicionario["fintech_cons"] *= random.randint(0, 50) / 100
        dicionario["fintech_int"] *= random.randint(-5, 75) / 100
        dicionario["fintech_arr"] *= random.randint(-10, 150) / 100

        dicionario["cripto_cons"] *= random.randint(0, 10) / 100
        dicionario["cripto_int"] *= random.randint(-10, 50) / 100
        dicionario["cripto_arr"] *= random.randint(-15, 75) / 100

    # Cenário 4: Bigtech crescem, fintech crescem e cripto caem
    elif cenario == 4:
        dicionario["bigtech_cons"] *= random.randint(0, 50) / 100
        dicionario["bigtech_int"] *= random.randint(-5, 75) / 100
        dicionario["bigtech_arr"] *= random.randint(-10, 150) / 100

        dicionario["fintech_cons"] *= random.randint(0, 50) / 100
        dicionario["fintech_int"] *= random.randint(-5, 75) / 100
        dicionario["fintech_arr"] *= random.randint(-10, 150) / 100

        dicionario["cripto_cons"] *= random.randint(-10, 5) / 100
        dicionario["cripto_int"] *= random.randint(-15, 10) / 100
        dicionario["cripto_arr"] *= random.randint(-50, 15) / 100

    # Cenário 5: Bigtech crescem, fintech caem e cripto crescem
    elif cenario == 5:
        dicionario["bigtech_cons"] *= random.randint(0, 50) / 100
        dicionario["bigtech_int"] *= random.randint(-5, 75) / 100
        dicionario["bigtech_arr"] *= random.randint(-10, 150) / 100

        dicionario["fintech_cons"] *= random.randint(-10, 5) / 100
        dicionario["fintech_int"] *= random.randint(-15, 10) / 100
        dicionario["fintech_arr"] *= random.randint(-50, 15) / 100

        dicionario["cripto_cons"] *= random.randint(0, 50) / 100
        dicionario["cripto_int"] *= random.randint(-5, 75) / 100
        dicionario["cripto_arr"] *= random.randint(-10, 150) / 100

    # Cenário 6: Bigtech caem, fintech crescem e cripto crescem
    elif cenario == 6:
        dicionario["bigtech_cons"] *= random.randint(-10, 5) / 100
        dicionario["bigtech_int"] *= random.randint(-15, 10) / 100
        dicionario["bigtech_arr"] *= random.randint(-50, 15) / 100

        dicionario["fintech_cons"] *= random.randint(0, 50) / 100
        dicionario["fintech_int"] *= random.randint(-5, 75) / 100
        dicionario["fintech_arr"] *= random.randint(-10, 150) / 100

        dicionario["cripto_cons"] *= random.randint(0, 50) / 100
        dicionario["cripto_int"] *= random.randint(-5, 75) / 100
        dicionario["cripto_arr"] *= random.randint(-10, 150) / 100

    # Cenário 7: Todas as ações crescem
    elif cenario == 7:
        dicionario["bigtech_cons"] *= random.randint(0, 50) / 100
        dicionario["bigtech_int"] *= random.randint(-5, 75) / 100
        dicionario["bigtech_arr"] *= random.randint(-10, 150) / 100

        dicionario["fintech_cons"] *= random.randint(0, 50) / 100
        dicionario["fintech_int"] *= random.randint(-5, 75) / 100
        dicionario["fintech_arr"] *= random.randint(-10, 150) / 100

        dicionario["cripto_cons"] *= random.randint(0, 50) / 100
        dicionario["cripto_int"] *= random.randint(-5, 75) / 100
        dicionario["cripto_arr"] *= random.randint(-10, 150) / 100

    # Cenário 8: Todas as ações caem
    elif cenario == 8:
        dicionario["bigtech_cons"] *= random.randint(-10, 5) / 100
        dicionario["bigtech_int"] *= random.randint(-15, 10) / 100
        dicionario["bigtech_arr"] *= random.randint(-50, 15) / 100

        dicionario["fintech_cons"] *= random.randint(-10, 5) / 100
        dicionario["fintech_int"] *= random.randint(-15, 10) / 100
        dicionario["fintech_arr"] *= random.randint(-50, 15) / 100

        dicionario["cripto_cons"] *= random.randint(-10, 5) / 100
        dicionario["cripto_int"] *= random.randint(-15, 10) / 100
        dicionario["cripto_arr"] *= random.randint(-50, 15) / 100

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
