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

        self.preco_comida = 400
        self.preco_aluguel = 400
        self.preco_remedio = 400


#Funcao Aluguel
    def aumentar_aluguel(self):
        try:    
            if self.aluguel< self.max_aluguel:
                self.aluguel += 1
                print(f"Aluguel: {self.aluguel}")
                self.dinheiro -= self.preco_aluguel
            else:
                print("Aluguel no máximo")
        except TypeError:
            print("Aluguel está no maximo")

    def diminuir_aluguel(self):
        try:
            if self.aluguel > 0:
                self.aluguel -= 1
                print(f"Aluguel: {self.aluguel}")
            else:
                print("Sem Aluguel")
        except TypeError:
            print("Aluguel não pode ser diminuido")

    def aumentar_max_aluguel(self, valor):
        if valor == 999:
            self.max_aluguel = "Infinito"
            self.aluguel = "Infinito"
        else:
            try:
                if self.aluguel == self.max_aluguel:
                    self.aluguel += valor
                self.max_aluguel += valor
            except TypeError:
                print("Valor Máximo Aluguel: Infinito")

#Funcao Comida
    def aumentar_comida(self):
        try:    
            if self.comida< self.max_comida:
                self.comida += 1
                print(f"Comida: {self.comida}")
                self.dinheiro -= self.preco_comida
            else:
                print("Comida no máximo")
        except TypeError:
            print("Comida está no maximo")

    def diminuir_comida(self):
        try:
            if self.comida > 0:
                self.comida -= 1
                print(f"comida: {self.comida}")
            else:
                print("Sem comida")
        except TypeError:
            print("comida não pode ser diminuido")

    def aumentar_max_comida(self, valor):
        if valor == 999:
            self.max_comida = "Infinito"
            self.comida = "Infinito"
        else:
            try:
                if self.comida == self.max_comida:
                    self.comida += valor
                self.max_comida += valor
            except TypeError:
                print("Valor Máximo comida: Infinito")

#Funcao Remedio
    def aumentar_remedio(self):
        try:    
            if self.remedio< self.max_remedio:
                self.remedio += 1
                print(f"remedio: {self.remedio}")
                self.dinheiro -= self.preco_remedio
            else:
                print("remedio no máximo")
        except TypeError:
            print("remedio está no maximo")

    def diminuir_remedio(self):
        try:
            if self.remedio > 0:
                self.remedio -= 1
                print(f"remedio: {self.remedio}")
            else:
                print("Sem remedio")
        except TypeError:
            print("remedio não pode ser diminuido")

    def aumentar_max_remedio(self, valor):
        if valor == 999:
            self.max_remedio = "Infinito"
            self.remedio = "Infinito"
        else:
            try:
                if self.remedio == self.max_remedio:
                    self.remedio += valor
                self.max_remedio += valor
            except TypeError:
                print("Valor Máximo remedio: Infinito")

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


    def comprar_item(self, preco):
        if self.dinheiro - preco < 0:
            return False
        else:
            self.dinheiro -= preco
            return True
        

#Preços Gastos
    def diminuir_preco_comida(self, valor):
        try:
            if self.preco_comida - valor < 0:
                self.preco_comida = 0
            else:
                self.preco_comida -= valor
        except TypeError:
            pass

    
    def diminuir_preco_aluguel(self, valor):
        try:
            if self.preco_aluguel - valor < 0:
                self.preco_aluguel = 0
            else:
                self.preco_aluguel -= valor
        except TypeError:
            pass


    def diminuir_preco_remedio(self, valor):
        try:
            if self.preco_remedio - valor < 0:
                self.preco_remedio = 0
            else:
                self.preco_remedio -= valor
        except TypeError:
            pass


# Reset dos staturs do player
    def reset(self):
        self.nome = ""
        self.dinheiro = 1500
        self.aluguel = 5
        self.max_aluguel = 5
        self.comida = 5
        self.max_comida = 5
        self.remedio = 5
        self.max_remedio = 5

        self.preco_comida = 400
        self.preco_aluguel = 400
        self.preco_remedio = 400
