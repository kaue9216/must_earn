class Player:
    def __init__(self, nome):
        self.nome = nome
        self.dinheiro = 1500
        self.vida = 5
        self.comida = 5
        self.remedio = 5

#Funcao Vida
    def aumentar_vida(self):
        if self.vida < 5:
            self.vida += 1
            print(f"Vida: {self.vida}")
        else:
            print("Vida no máximo")

    def diminuir_vida(self):
        if self.vida > 0:
            self.vida -= 1
            print(f"Vida: {self.vida}")
        else:
            print("Sem vida")

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

#Remedio
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
