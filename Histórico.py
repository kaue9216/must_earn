b =[]

def adicionar_historico(aluguel, comida, remedio, saldo, lista_b):
    a = {"aluguel":aluguel, "comida":comida, "remedio": remedio, "saldo":saldo}
    lista_b.append(a)

aluguel = 1
comida = 1
remedio = 1
saldo = 1
teste = 0
while teste < 5:
    adicionar_historico(aluguel, comida, remedio, saldo, b)
    teste = teste+1

for x in b:
    print(x)