class Player:
    def __init__(self):
        self.nome = ""
        self.dinheiro = 1500
        self.aluguel = 5
        self.max_aluguel = 5
        self.comida = 5
        self.max_comida = 5
        self.remedio = 5
        self.max_remedio = 5

#Funcao Aluguel
    def aumentar_aluguel(self):
        if self.aluguel< 5:
            self.aluguel += 1
            print(f"Aluguel: {self.aluguel}")
            self.dinheiro -= 400
        else:
            print("Aluguel no máximo")

    def diminuir_aluguel(self):
        if self.aluguel > 0:
            self.aluguel -= 1
            print(f"Aluguel: {self.aluguel}")
        else:
            print("Sem Aluguel")

#Funcao Comida
    def aumentar_comida(self):
        if self.comida < 5:
            self.comida += 1
            print(f"Comida: {self.comida} ")
            self.dinheiro -= 400
        else:
            print("Comida no máximo")

    def diminuir_comida(self):
        if self.comida > 0:
            self.comida -= 1
            print(f"Comida: {self.comida}")
        else:
            print("Sem comida")

#Funcao Remedio
    def aumentar_remedio(self):
        if self.remedio < 5:
            self.remedio += 1
            print(f"Remédio: {self.remedio}")
            self.dinheiro -= 400
        else:
            print("Remédio no máximo")

    def diminuir_remedio(self):
        if self.remedio > 0:
            self.remedio -= 1
            print(f"Remédio: {self.remedio}")
        else:
            print("Sem Remédio")

#Funcao Dinheiro
    def resultado_investimentos(self, dicionario_investimentos_iniciais, dicionario_atualizado):
        lucro_total_rodada = 0
        for key in dicionario_investimentos_iniciais.keys():
            self.dinheiro += dicionario_atualizado[key]
            lucro_total_rodada += dicionario_atualizado[key] - dicionario_investimentos_iniciais[key]
        return lucro_total_rodada
        

    def aplicar_dinheiro(self,valor):
        if self.dinheiro >= valor:
            self.dinheiro -= valor
            return True
        else:
            return False

    def receber_dinheiro(self, valor):
        self.dinheiro += valor


    def reset(self):
        self.nome = ""
        self.dinheiro = 1500
        self.aluguel = 5
        self.max_aluguel = 5
        self.comida = 5
        self.max_comida = 5
        self.remedio = 5
        self.max_remedio = 5
