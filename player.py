class Player:
    def __init__(self):
        self.nome = "João Pedro"
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
        else:
            print("Comida no máximo")

    def diminuir_comida(self):
        if self.comida > 0:
            self.comida -= 1
            print(f"Comida: {self.comida}")
        else:
            print("Sem comida")

#Funcao Remedio
    def aumentar_remdio(self):
        if self.remedio < 5:
            self.remedio += 1
            print(f"Remédio: {self.remedio}")
        else:
            print("Remédio no máximo")

    def diminuir_remedio(self):
        if self.remedio > 0:
            self.remedio -= 1
            print(f"Remédio: {self.remedio}")
        else:
            print("Sem Remédio")

#Funcao Dinheiro
    def adicionar_dinheiro(self, valor):
        self.dinheiro += valor

    def aplicar_dinheiro(self,valor):
        if self.dinheiro >= valor:
            self.dinheiro -= valor
        else:
            print("Dinheiro Insuficiente")

#Maximo aluguel
    def aumemtar_max_aluguel(self, valor_alteracao):
        self.max_aluguel += valor_alteracao
        print(self.max_aluguel)

# Máximo comida
    def aumentar_max_comida(self, valor_alteracao):
        self.max_comida += valor_alteracao
        print(self.max_comida)

# Máximo remédio
    def aumentar_max_remedio(self, valor_alteracao):
        self.max_remedio += valor_alteracao
        print(self.max_remedio)
