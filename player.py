class Player:
    def __init__(self):
        # ATRIBUTOS DO PLAYER
        self.nome = ""
        self.dinheiro = 1500
        self.aluguel = 5
        self.max_aluguel = 5
        self.comida = 5
        self.max_comida = 5
        self.remedio = 5
        self.max_remedio = 5
        
        self.lucro_total_partida = 0
        self.rodadas = 0

        self.preco_comida = 400
        self.preco_aluguel = 400
        self.preco_remedio = 400


#Funcao Aluguel
    def aumentar_aluguel(self): # Aumenta o aluguel quando comprado
        try:    
            if self.aluguel< self.max_aluguel:
                self.aluguel += 1
                print(f"Aluguel: {self.aluguel}")
                self.dinheiro -= self.preco_aluguel
            else:
                print("Aluguel no máximo")
        except TypeError:
            print("Aluguel está no maximo")

    def diminuir_aluguel(self):# Diminui o aluguel quando acaba a rodada
        try:
            if self.aluguel > 0:
                self.aluguel -= 1
                print(f"Aluguel: {self.aluguel}")
            else:
                print("Sem Aluguel")
        except TypeError:
            print("Aluguel não pode ser diminuido")

    def aumentar_max_aluguel(self, valor): # aumenta o valor maximo do aluguel, se estiver em infinito, deixa infinito
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

    
    def texto_status_aluguel(self):
        try:
            ponto_aluguel = []
            for i in range(1, self.max_aluguel + 1):
                if i <= self.aluguel:
                    ponto_aluguel.append("🟩")
                else:
                    ponto_aluguel.append("⬛")
            
            pontos = ""
            for p in ponto_aluguel:
                pontos += p
            return pontos
        except TypeError:
            return "Infinito"
            
            

#Funcao Comida
    def aumentar_comida(self):  # Aumenta a comida quando comprado
        try:    
            if self.comida< self.max_comida:
                self.comida += 1
                print(f"Comida: {self.comida}")
                self.dinheiro -= self.preco_comida
            else:
                print("Comida no máximo")
        except TypeError:
            print("Comida está no maximo")

    def diminuir_comida(self): # Diminui a comida quando acaba a rodada
        try:
            if self.comida > 0:
                self.comida -= 1
                print(f"comida: {self.comida}")
            else:
                print("Sem comida")
        except TypeError:
            print("comida não pode ser diminuido")

    def aumentar_max_comida(self, valor): # aumenta o valor maximo da comida, se estiver em infinito, deixa infinito
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


    def texto_status_comida(self):
        try:
            ponto_comida = []
            for i in range(1, self.max_comida + 1):
                if i <= self.comida:
                    ponto_comida.append("🟩")
                else:
                    ponto_comida.append("⬛")
            
            pontos = ""
            for p in ponto_comida:
                pontos += p
            return pontos
        except TypeError:
            return "Infinito"


#Funcao Remedio
    def aumentar_remedio(self): # Aumenta o remedio quando comprado
        try:    
            if self.remedio< self.max_remedio:
                self.remedio += 1
                print(f"remedio: {self.remedio}")
                self.dinheiro -= self.preco_remedio
            else:
                print("remedio no máximo")
        except TypeError:
            print("remedio está no maximo")

    def diminuir_remedio(self): # Diminui o remedio quando acaba a rodada
        try:
            if self.remedio > 0:
                self.remedio -= 1
                print(f"remedio: {self.remedio}")
            else:
                print("Sem remedio")
        except TypeError:
            print("remedio não pode ser diminuido")

    def aumentar_max_remedio(self, valor): # aumenta o valor maximo do remedio, se estiver em infinito, deixa infinito
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

    def texto_status_remedio(self):
        try:
            ponto_remedio = []
            for i in range(1, self.max_remedio + 1):
                if i <= self.remedio:
                    ponto_remedio.append("🟩")
                else:
                    ponto_remedio.append("⬛")
            
            pontos = ""
            for p in ponto_remedio:
                pontos += p
            return pontos
        except TypeError:
            return "Infinito"


#Funcao Dinheiro
    # Pega o investimento inicial, e o valor que rendeu
    def resultado_investimentos(self, dicionario_investimentos_iniciais, dicionario_atualizado):
        lucro_total_rodada = 0 # cria o lucro da rodada
        for key in dicionario_investimentos_iniciais.keys(): # passa por todos os investimentos, e adiciona o valor que rendeu
            self.dinheiro += dicionario_atualizado[key]
            lucro_total_rodada += dicionario_atualizado[key] - dicionario_investimentos_iniciais[key] # adiciona o lucro a rodada
        
        self.lucro_total_partida += lucro_total_rodada # Adiciona ao lucro total
        return lucro_total_rodada # retorna o lucro que ira ser printado no jornal


    def aplicar_dinheiro(self,valor): # FAZ A CONTA DE APLICAR O DINHEIRO, E SE PLAYER POSSUI SALDO
        if self.dinheiro >= valor:
            self.dinheiro -= valor
            return True
        else:
            return False

    def receber_dinheiro(self, valor): # QUANDO RECEBE DINHEIRO, SOMA AO TOTAL
        self.dinheiro += valor


    def comprar_item(self, preco): # CHECA O SALDO, E DESCONTA DO DINHEIRO TOTAL O VALOR DO ITEM, E CASO SALDO INDISPONIVEL RETORNA FALSO
        if self.dinheiro - preco < 0:
            return False
        else:
            self.dinheiro -= preco
            return True
        

#Preços Gastos
    def diminuir_preco_comida(self, valor): # DIMINUI O PREÇO DA COMIDA
        try:
            if self.preco_comida - valor < 0:
                self.preco_comida = 0
            else:
                self.preco_comida -= valor
        except TypeError:
            pass

    
    def diminuir_preco_aluguel(self, valor):# DIMINUI O PREÇO DO ALUGUEL
        try:
            if self.preco_aluguel - valor < 0:
                self.preco_aluguel = 0
            else:
                self.preco_aluguel -= valor
        except TypeError:
            pass


    def diminuir_preco_remedio(self, valor):# DIMINUI O PREÇO DO REMEDIO
        try:
            if self.preco_remedio - valor < 0:
                self.preco_remedio = 0
            else:
                self.preco_remedio -= valor
        except TypeError:
            pass

    
    def aumentar_rodada(self):
        self.rodadas += 1


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

        self.lucro_total_partida = 0
        self.rodadas = 0

        self.preco_comida = 400
        self.preco_aluguel = 400
        self.preco_remedio = 400