# acoesv2.py
import random

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


