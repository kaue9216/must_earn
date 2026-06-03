# acoesv2.py
import random

def aplicar_cenario(dicionario):  # Removido o parâmetro cenario daqui
    # O sorteio acontece unicamente aqui dentro agora
    cenario = random.randint(1, 8)

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

    # Retorna o dicionário modificado E o número do cenário sorteado
    return dicionario, cenario


