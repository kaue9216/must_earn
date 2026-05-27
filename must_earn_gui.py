import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QTextEdit, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout


class MustEarn(QWidget):
    def __init__(self):
        super().__init__()

        self.titulo = QLabel("MUST EARN")


        self.hp = QLabel(f"Saúde: {5}", self)
        self.comida = QLabel(f"Comida: {5}", self)
        self.remedio = QLabel(f"Remédio: {5}", self)
        self.saldo = QLabel(f"Saldo: R${999.99}", self)


        self.jornal = QTextEdit(self)
        self.jornal.setReadOnly(True)
        self.jornal.setFontPointSize(16)
        self.jornal.setPlainText("Bem-vindo a Must Earn")
        self.jornal.append("Dudeckson\n" * 50)


        self.acao_1 = QLineEdit(self)
        self.acao_1.setPlaceholderText("R$ 0.00")
        self.acao_2 = QLineEdit(self)
        self.acao_2.setPlaceholderText("R$ 0.00")
        self.acao_3 = QLineEdit(self)
        self.acao_3.setPlaceholderText("R$ 0.00")

        self.acao_4 = QLineEdit(self)
        self.acao_4.setPlaceholderText("R$ 0.00")
        self.acao_5 = QLineEdit(self)
        self.acao_5.setPlaceholderText("R$ 0.00")
        self.acao_6 = QLineEdit(self)
        self.acao_6.setPlaceholderText("R$ 0.00")

        self.acao_7 = QLineEdit(self)
        self.acao_7.setPlaceholderText("R$ 0.00")
        self.acao_8 = QLineEdit(self)
        self.acao_8.setPlaceholderText("R$ 0.00")
        self.acao_9 = QLineEdit(self)
        self.acao_9.setPlaceholderText("R$ 0.00")

        
        self.botao_jogar = QPushButton("Jogar", self)

        self.botao_loja = QPushButton("Loja", self)

        self.initUi()

    
    def initUi(self):
        self.setWindowTitle("MUST EARN")

        vbox = QVBoxLayout()
        
        
        vbox.addWidget(self.titulo)

        
        hbox_status = QHBoxLayout()
        hbox_status.addWidget(self.hp)
        hbox_status.addWidget(self.comida)
        hbox_status.addWidget(self.remedio)
        hbox_status.addWidget(self.saldo)

        vbox.addLayout(hbox_status)


        vbox.addWidget(self.jornal)


        hbox_col_acoes_1 = QHBoxLayout()
        hbox_col_acoes_1.addWidget(self.acao_1)
        hbox_col_acoes_1.addWidget(self.acao_2)
        hbox_col_acoes_1.addWidget(self.acao_3)

        hbox_col_acoes_2 = QHBoxLayout()
        hbox_col_acoes_2.addWidget(self.acao_4)
        hbox_col_acoes_2.addWidget(self.acao_5)
        hbox_col_acoes_2.addWidget(self.acao_6)
        
        hbox_col_acoes_3 = QHBoxLayout()
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

        print(self.jornal.toPlainText())

        
        



if __name__ == "__main__":
    app = QApplication(sys.argv)
    must_earn = MustEarn()
    must_earn.show()
    sys.exit(app.exec_())
