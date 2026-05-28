import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QTextEdit, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout
import acoesv2
import random
import textos


class MustEarn(QWidget):
    def __init__(self):
        super().__init__()

        self.titulo = QLabel("MUST EARN")


        self.comida = QLabel(f"Comida: {5}", self)
        self.remedio = QLabel(f"Remédio: {5}", self)
        self.salario = QLabel(f"Salário: {5}", self)
        self.saldo = QLabel(f"Saldo: R${999.99}", self)


        self.jornal = QTextEdit(self)
        self.jornal.setReadOnly(True)
        self.jornal.setFontPointSize(16)
        self.jornal.setPlainText("Bem-vindo a Must Earn")
        self.jornal.append("=" * 30)
        self.jornal.append("LORE DO MERCADO:")
        self.jornal.append("=" * 30)
        self.jornal.append(textos.lore)


        self.acao_1 = QLineEdit(self)
        self.acao_1.setPlaceholderText("0.00")
        self.acao_2 = QLineEdit(self)
        self.acao_2.setPlaceholderText("0.00")
        self.acao_3 = QLineEdit(self)
        self.acao_3.setPlaceholderText("0.00")

        self.acao_4 = QLineEdit(self)
        self.acao_4.setPlaceholderText("0.00")
        self.acao_5 = QLineEdit(self)
        self.acao_5.setPlaceholderText("0.00")
        self.acao_6 = QLineEdit(self)
        self.acao_6.setPlaceholderText("0.00")

        self.acao_7 = QLineEdit(self)
        self.acao_7.setPlaceholderText("0.00")
        self.acao_8 = QLineEdit(self)
        self.acao_8.setPlaceholderText("0.00")
        self.acao_9 = QLineEdit(self)
        self.acao_9.setPlaceholderText("0.00")


        self.col_acoes_1 = QLabel("Big Techs", self)
        self.col_acoes_2 = QLabel("Fintechs", self)
        self.col_acoes_3 = QLabel("Cripto", self)

        
        self.risco_cons = QLabel("C", self)
        self.risco_int = QLabel("I", self)
        self.risco_arr = QLabel("A", self)

        
        self.botao_jogar = QPushButton("Jogar", self)

        self.botao_loja = QPushButton("Loja", self)

        self.initUi()

    
    def initUi(self):
        self.setWindowTitle("MUST EARN")

        vbox = QVBoxLayout()
        
        
        vbox.addWidget(self.titulo)

        
        hbox_status = QHBoxLayout()
        hbox_status.addWidget(self.comida)
        hbox_status.addWidget(self.remedio)
        hbox_status.addWidget(self.salario)
        hbox_status.addWidget(self.saldo)

        vbox.addLayout(hbox_status)


        vbox.addWidget(self.jornal)


        hbox_acoes_titulos = QHBoxLayout()
        hbox_acoes_titulos.addWidget(self.col_acoes_1)
        hbox_acoes_titulos.addWidget(self.col_acoes_2)
        hbox_acoes_titulos.addWidget(self.col_acoes_3)

        vbox.addLayout(hbox_acoes_titulos)


        hbox_col_acoes_1 = QHBoxLayout()
        hbox_col_acoes_1.addWidget(self.risco_cons)
        hbox_col_acoes_1.addWidget(self.acao_1)
        hbox_col_acoes_1.addWidget(self.acao_2)
        hbox_col_acoes_1.addWidget(self.acao_3)

        hbox_col_acoes_2 = QHBoxLayout()
        hbox_col_acoes_2.addWidget(self.risco_int)
        hbox_col_acoes_2.addWidget(self.acao_4)
        hbox_col_acoes_2.addWidget(self.acao_5)
        hbox_col_acoes_2.addWidget(self.acao_6)
        
        hbox_col_acoes_3 = QHBoxLayout()
        hbox_col_acoes_3.addWidget(self.risco_arr)
        hbox_col_acoes_3.addWidget(self.acao_7)
        hbox_col_acoes_3.addWidget(self.acao_8)
        hbox_col_acoes_3.addWidget(self.acao_9)

        vbox_acoes = QVBoxLayout()
        vbox_acoes.addLayout(hbox_col_acoes_1)
        vbox_acoes.addLayout(hbox_col_acoes_2)
        vbox_acoes.addLayout(hbox_col_acoes_3)

        vbox.addLayout(vbox_acoes)

        
        vbox.addWidget(self.botao_jogar)

        vbox.addWidget(self.botao_loja)

        self.setLayout(vbox)

        
        self.acoes_valores = [self.acao_1, self.acao_2, self.acao_3,
                         self.acao_4, self.acao_5, self.acao_6,
                         self.acao_7, self.acao_8, self.acao_9]
        
        self.valores_lista = []
        
        self.botao_jogar.clicked.connect(self.inicializar_dados_acoes)
        




    def get_valores_investidos(self, acoes_valores: list):
        valores = []

        for acao in acoes_valores:
            try:
                if acao.text() == "":
                    valor = float(acao.placeholderText())
                    valores.append(valor)
                else:
                    valor = float(acao.text())
                    valores.append(valor)
            except ValueError:
                self.jornal.append("--Os valores investidos devem ser um número--")
                acao.clear()
                return None
        
        dicionario_ativos = {
            "bigtech_cons" : float(valores[0]), 
            "bigtech_int" : float(valores[3]), 
            "bigtech_arr" : float(valores[6]),

            "fintech_cons" : float(valores[1]), 
            "fintech_int" : float(valores[4]), 
            "fintech_arr" : float(valores[7]),

            "cripto_cons" : float(valores[2]), 
            "cripto_int" : float(valores[5]), 
            "cripto_arr" : float(valores[8])
        }

        return dicionario_ativos


    def inicializar_dados_acoes(self):
        # --- Inicialização dos Dados ---
        dicionario_ativos = self.get_valores_investidos(self.acoes_valores)
        if dicionario_ativos is None:
            return

        lista = [1, 2, 3, 4, 5, 6, 7, 8]
        escolha_cenario = random.randint(0, 7)
        cenario_sorteado = lista[escolha_cenario]


        # --- Processamento ---
        # 1. Aplica o cálculo matemático no dicionário
        dicionario_atualizado = acoesv2.aplicar_cenario(cenario_sorteado, dicionario_ativos)

        # 2. Puxa o texto correspondente do arquivo textos.py usando o id do cenário
        texto_do_cenario = textos.cenarios.get(cenario_sorteado)


        # --- Outputs Formatados no Terminal ---
        self.jornal.append("=" * 30)
        self.jornal.append(f"NOTÍCIA DO CENÁRIO SORTEADO (Cenário {cenario_sorteado}):")
        self.jornal.append("=" * 30)
        self.jornal.append(texto_do_cenario)
        self.jornal.append("\n" + "=" * 30)
        self.jornal.append("VALOR ATUALIZADO DOS ATIVOS POST-PREGÃO:")
        self.jornal.append("=" * 30)
        for ativo, valor in dicionario_atualizado.items():
            self.jornal.append(f"{ativo}: {valor:.4f}")
        self.jornal.append("=" * 30)
                
                        
        
        



if __name__ == "__main__":
    app = QApplication(sys.argv)
    must_earn = MustEarn()
    must_earn.show()
    sys.exit(app.exec_())
