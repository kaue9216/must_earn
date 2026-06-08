import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QTextEdit, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QDialog
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import acoesv2
import random
import textos
from player import Player
import powerups
import Histórico


class Login(QWidget):
    def __init__(self):
        super().__init__()


        self.titulo = QLabel()
        self.fred_fl_img = QLabel()
        self.texto_login = QLabel("Insira o nome de usuário:")
        self.username = QLineEdit()
        self.erro_texto = QLabel("")
        self.botao_login = QPushButton("JOGAR")


        self.initUi()

        self.setStyleSheet("""
QWidget {
    background-color: #020406;
    color: #2DE2E6;
    font-family: Consolas;
}
""")


    def initUi(self):
        self.setWindowTitle("MUST EARN")
        self.setFixedSize(900, 850)

        self.setStyleSheet("""
QWidget {
    background-color: #020406;
    color: #2DE2E6;
    font-family: Consolas;
}

QLineEdit {
    background-color: #071014;
    color: #39FF88;
    border: 2px solid #2DE2E6;
    border-radius: 8px;
    padding: 5px;
}

QPushButton {
    background-color: #071014;
    color: #39FF88;
    border: 2px solid #39FF88;
    border-radius: 10px;
    padding: 10px;
    font-weight: bold;
}

QPushButton:hover {
    background-color: #39FF88;
    color: black;
}

QTextEdit {
    background-color: #071014;
    color: #39FF88;
    border: 2px solid #2DE2E6;
}
""")

        vbox = QVBoxLayout()
        vbox.setAlignment(Qt.AlignTop | Qt.AlignCenter)
        vbox.setSpacing(30)


        pixmap_titulo = QPixmap("./must_earn_logo.jpeg")
        pixmap_titulo = pixmap_titulo.scaled(
            512,
            288,
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation   
        )
        self.titulo.setPixmap(pixmap_titulo)
        self.titulo.setAlignment(Qt.AlignCenter)
        vbox.addWidget(self.titulo)

        self.titulo.setAlignment(Qt.AlignCenter)



        pixmap = QPixmap("./must_earn.jpeg")
        pixmap = pixmap.scaled(
            650,
            450,
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )
        self.fred_fl_img.setPixmap(pixmap)
        self.fred_fl_img.setAlignment(Qt.AlignCenter)
        vbox.addWidget(self.fred_fl_img)


        self.texto_login.setAlignment(Qt.AlignCenter)
        vbox.addWidget(self.texto_login)


        self.username.setAlignment(Qt.AlignCenter)
        self.username.setPlaceholderText("Usuário...")
        self.username.setFixedSize(500, 60)
        vbox.addWidget(self.username, alignment=Qt.AlignCenter)

        self.erro_texto.setAlignment(Qt.AlignCenter)
        self.erro_texto.setStyleSheet("""
color: #FF2C2C;
font-size: 20px;
font-weight: bold; 
""")
        vbox.addWidget(self.erro_texto)


        self.botao_login.setFixedSize(300, 80)
        self.botao_login.setCursor(Qt.PointingHandCursor)
        vbox.addWidget(self.botao_login, alignment=Qt.AlignCenter)


        self.setLayout(vbox)


        self.fred_fl_img.setObjectName("fred_fl_img")
        self.texto_login.setObjectName("texto_login")

        self.texto_login.setStyleSheet("""
color: #39FF88;
font-size: 20px;
font-weight: bold;
""")

        self.username.setObjectName("username")

        self.username.setStyleSheet("""
QLineEdit {
    background-color: #071014;
    color: #39FF88;
    border: 2px solid #2DE2E6;
    border-radius: 10px;
    padding-left: 20px;
    font-size: 18px;
    font-weight: bold;
}

QLineEdit:focus {
    border: 2px solid #39FF88;
}
""")


        self.botao_login.setObjectName("botao_login")




        self.botao_login.clicked.connect(self.checar_usuario)

        self.botao_login.setStyleSheet("""
QPushButton {
    background-color: #071014;
    color: #39FF88;
    border: 2px solid #39FF88;
    border-radius: 10px;
    font-size: 22px;
    font-weight: bold;
}

QPushButton:hover {
    background-color: #39FF88;
    color: black;
}

QPushButton:pressed {
    background-color: #2DE2E6;
    color: black;
}
""")


    def checar_usuario(self): # CHECA SE O USUARIO INSERIU UM USERNAME, SE SIM VAI PARA A TELA PRINCIPAL DO JOGO
        if self.username.text():
            if Histórico.validar_nome_disponivel(self.username.text()):
                player.nome = self.username.text()
                self.must_earn = MustEarn()
                self.must_earn.show()
                self.close()
            else:
                self.username.clear()
                self.erro_texto.setText("Nome de usuário já utilizado")
        else:
            self.erro_texto.setText("Você deve inserir um nome de usuário")


class GastosDiarios(QDialog):
    def __init__(self):
        super().__init__()


        self.comida_status = QLabel(f"Comida: {player.comida}", self)
        self.remedio_status = QLabel(f"Remédio: {player.remedio}", self)
        self.aluguel_status = QLabel(f"Aluguel: {player.aluguel}", self)
        self.saldo_status = QLabel(f"Saldo: R${player.dinheiro:.2f}", self)

        self.comida_txt = QLabel("COMIDA")
        self.comida_img = QLabel()
        self.comida_botao = QPushButton(f"Comprar R${str(player.preco_comida)}")

        self.remedio_txt = QLabel("REMÉDIO")
        self.remedio_img = QLabel()
        self.remedio_botao = QPushButton(f"Comprar R${str(player.preco_remedio)}")

        self.aluguel_txt = QLabel("ALUGUEL")
        self.aluguel_img = QLabel()
        self.aluguel_botao = QPushButton(f"Comprar R${player.preco_aluguel}")

        self.aviso = QLabel("")

        self.fechar = QPushButton("Fechar")

        self.initUi()


    def initUi(self):
        self.setWindowTitle("MUST EARN")
        self.setFixedSize(1200, 700)

        for lbl in [self.comida_status, self.remedio_status,
            self.aluguel_status, self.saldo_status]:
            lbl.setStyleSheet("""
    color: #2DE2E6;
    font-size: 18px;
    font-weight: bold;
    """)

        self.setStyleSheet("""
QDialog {
    background-color: #020406;
    color: #2DE2E6;
    font-family: Consolas;
}

QLabel {
    color: #D6F5FF;
    font-size: 16px;
    font-weight: bold;
}

QPushButton {
    background-color: #071014;
    color: #39FF88;
    border: 2px solid #39FF88;
    border-radius: 10px;
    padding: 10px;
    font-size: 16px;
    font-weight: bold;
}

QPushButton:hover {
    background-color: #39FF88;
    color: black;
}

QPushButton:pressed {
    background-color: #2DE2E6;
    color: black;
}
""")

        self.comida_txt.setStyleSheet("""
color: #39FF88;
font-size: 22px;
font-weight: 900;
""")

        self.remedio_txt.setStyleSheet("""
color: #39FF88;
font-size: 22px;
font-weight: 900;
""")

        self.aluguel_txt.setStyleSheet("""
color: #39FF88;
font-size: 22px;
font-weight: 900;
""")


        vbox = QVBoxLayout()
        vbox.setAlignment(Qt.AlignTop | Qt.AlignCenter)
        vbox.setSpacing(30)


        hbox_status = QHBoxLayout()
        hbox_status.addWidget(self.comida_status)
        hbox_status.addWidget(self.remedio_status)
        hbox_status.addWidget(self.aluguel_status)
        hbox_status.addWidget(self.saldo_status)

        vbox.addLayout(hbox_status)


        hbox_opcoes = QHBoxLayout()
        hbox_opcoes.setAlignment(Qt.AlignTop | Qt.AlignCenter)
        hbox_opcoes.setSpacing(30)


        vbox_comida = QVBoxLayout()
        vbox_comida.addWidget(self.comida_txt, alignment=Qt.AlignCenter)
        vbox_comida.addWidget(self.comida_img)
        pixmap_comida = QPixmap("./must_earn_comida.jpeg")
        pixmap_comida = pixmap_comida.scaled(
            300,
            400,
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )
        self.comida_img.setPixmap(pixmap_comida)
        vbox_comida.addWidget(self.comida_botao)
        vbox_comida.setAlignment(Qt.AlignCenter)
        hbox_opcoes.addLayout(vbox_comida)

        vbox_remedio = QVBoxLayout()
        vbox_remedio.addWidget(self.remedio_txt, alignment=Qt.AlignCenter)
        vbox_remedio.addWidget(self.remedio_img)
        pixmap_remedio = QPixmap("./must_earn_remedio.jpeg")
        pixmap_remedio = pixmap_remedio.scaled(
            300,
            400,
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )
        self.remedio_img.setPixmap(pixmap_remedio)
        vbox_remedio.addWidget(self.remedio_botao)
        vbox_remedio.setAlignment(Qt.AlignCenter)
        hbox_opcoes.addLayout(vbox_remedio)

        vbox_aluguel = QVBoxLayout()
        vbox_aluguel.addWidget(self.aluguel_txt, alignment=Qt.AlignCenter)
        vbox_aluguel.addWidget(self.aluguel_img)
        pixmap_aluguel = QPixmap("./must_earn_aluguel.jpeg")
        pixmap_aluguel = pixmap_aluguel.scaled(
            300,
            400,
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )
        self.aluguel_img.setPixmap(pixmap_aluguel)
        vbox_aluguel.addWidget(self.aluguel_botao)
        vbox_aluguel.setAlignment(Qt.AlignCenter)
        hbox_opcoes.addLayout(vbox_aluguel)
        hbox_opcoes.setSpacing(30)

        vbox.addLayout(hbox_opcoes)

        vbox.addWidget(self.aviso)
        self.aviso.setAlignment(Qt.AlignCenter)

        self.aviso.setStyleSheet("""
color: #FF5555;
font-size: 18px;
font-weight: bold;
""")

        vbox.addWidget(self.fechar, alignment=Qt.AlignCenter)

        self.setLayout(vbox)

        self.atualizar_status()

        self.comida_botao.clicked.connect(self.comprar_comida)
        self.remedio_botao.clicked.connect(self.comprar_remedio)
        self.aluguel_botao.clicked.connect(self.comprar_aluguel)

        self.fechar.clicked.connect(self.accept)



        
    
    def comprar_comida(self): # CHECA SE O JOGADOR ESTA COM O STATUS NO MAXIMO OU SE NAO TEM DINHEIRO PARA COMPRAR, SE NAO COMPRA O STATUS
        if player.comida == player.max_comida:
            self.aviso.setText("Comida já está no maximo")
            return        
        if player.dinheiro < player.preco_comida:
            self.aviso.setText("Saldo Insuficiente")
            return
        player.aumentar_comida()
        self.atualizar_status()


    def comprar_remedio(self): # CHECA SE O JOGADOR ESTA COM O STATUS NO MAXIMO OU SE NAO TEM DINHEIRO PARA COMPRAR, SE NAO COMPRA O STATUS
        if player.remedio == player.max_remedio:
            self.aviso.setText("Remédio já está no maximo")
            return        
        if player.dinheiro < player.preco_remedio:
            self.aviso.setText("Saldo Insuficiente")
            return
        player.aumentar_remedio()
        self.atualizar_status()


    def comprar_aluguel(self): # CHECA SE O JOGADOR ESTA COM O STATUS NO MAXIMO OU SE NAO TEM DINHEIRO PARA COMPRAR, SE NAO COMPRA O STATUS
        if player.aluguel == player.max_aluguel:
            self.aviso.setText("Aluguel já está no maximo")
            return
        if player.dinheiro < player.preco_aluguel:
            self.aviso.setText("Saldo Insuficiente")
            return
        player.aumentar_aluguel()
        self.atualizar_status()


    def atualizar_status(self): # ATUALIZA OS STATUS SEMPRE QUE ALGUM ATRIBUTO É COMPRADO
        self.comida_status.setText(f"Comida: {str(player.comida)}/{str(player.max_comida)}")
        self.remedio_status.setText(f"Remédio: {str(player.remedio)}/{str(player.max_remedio)}")
        self.aluguel_status.setText(f"Aluguel: {str(player.aluguel)}/{str(player.max_aluguel)}")
        
        self.saldo_status.setText(f"Saldo: R${str(round(player.dinheiro, 2))}")
        
        self.comida_botao.setText(f"Comprar R${player.preco_comida}")
        self.remedio_botao.setText(f"Comprar R${player.preco_remedio}")
        self.aluguel_botao.setText(f"Comprar R${player.preco_aluguel}")


class GameOver(QDialog):
    def __init__(self, must_earn):
        super().__init__()
        self.must_earn = must_earn

        self.titulo = QLabel()
        self.game_over_img = QLabel()
        self.botao_restart = QPushButton("Jogar de Novo")
        self.botao_sair = QPushButton("Sair")

        self.initUi()


    def initUi(self):
        self.setWindowTitle("MUST EARN")
        self.setFixedSize(900, 850)

        self.setStyleSheet("""
QWidget {
    background-color: #020406;
    color: #FF3131;
    font-family: Consolas;
}

QPushButton {
    background-color: #120505;
    color: #FF3131;
    border: 2px solid #FF3131;
    border-radius: 10px;
    padding: 10px;
    font-size: 22px;
    font-weight: bold;
}

QPushButton:hover {
    background-color: #FF3131;
    color: black;
}

QPushButton:pressed {
    background-color: #FF6666;
    color: black;
}
""")

        # Título
        pixmap_titulo = QPixmap("./must_earn_logo.jpeg")
        pixmap_titulo = pixmap_titulo.scaled(
            512,
            250,
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation   
        )
        self.titulo.setPixmap(pixmap_titulo)
        self.titulo.setAlignment(Qt.AlignCenter)


        vbox = QVBoxLayout()
        vbox.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        vbox.setSpacing(30)

        vbox.addWidget(self.titulo)

        pixmap_game_over = QPixmap("./must_earn_TelaDeDerrota.jpeg")
        pixmap_game_over = pixmap_game_over.scaled(
            650,
            500,
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )

        self.game_over_img.setPixmap(pixmap_game_over)
        self.game_over_img.setAlignment(Qt.AlignCenter)

        vbox.addWidget(self.game_over_img)


        self.botao_restart.setFixedSize(300, 80)
        self.botao_restart.setCursor(Qt.PointingHandCursor)

        vbox.addWidget(self.botao_restart, alignment=Qt.AlignCenter)

        self.botao_sair.setFixedSize(300, 80)
        self.botao_sair.setCursor(Qt.PointingHandCursor)

        vbox.addWidget(self.botao_sair, alignment=Qt.AlignCenter)

        self.setLayout(vbox)


        self.botao_restart.clicked.connect(self.restart)
        self.botao_sair.clicked.connect(self.sair_do_jogo)


    def restart(self): # RESETA OS STATUS DO PLAYER, FECHA A JANELA PRINCIPAL E REABRE A JANELA DE LOGIN
        player.reset()
        self.login = Login()
        self.login.show()
        self.must_earn.close()
        self.accept()


    def sair_do_jogo(self): # FECHA O JOGO
        QApplication.quit()


class TelaDaVitoria(QDialog):
    def __init__(self, must_earn):
        super().__init__()
        self.must_earn = must_earn

        self.titulo = QLabel("MUST EARN")
        self.tela_vitoria_img = QLabel()
        self.botao_restart = QPushButton("Jogar de Novo")
        self.botao_sair = QPushButton("Sair")

        self.initUi()


    def initUi(self):
        self.setWindowTitle("MUST EARN")
        self.setFixedSize(900, 850)

        self.setStyleSheet("""
QWidget {
    background-color: #020406;
    color: #2DE2E6;
    font-family: Consolas;
}

QPushButton {
    background-color: #071014;
    color: #39FF88;
    border: 2px solid #39FF88;
    border-radius: 10px;
    padding: 10px;
    font-size: 22px;
    font-weight: bold;
}

QPushButton:hover {
    background-color: #39FF88;
    color: black;
}

QPushButton:pressed {
    background-color: #2DE2E6;
    color: black;
}
""")

        vbox = QVBoxLayout()
        vbox.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        vbox.setSpacing(30)


        pixmap_titulo = QPixmap("./must_earn_logo.jpeg")
        pixmap_titulo = pixmap_titulo.scaled(
            512,
            288,
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation   
        )
        self.titulo.setPixmap(pixmap_titulo)
        self.titulo.setAlignment(Qt.AlignCenter)

        vbox.addWidget(self.titulo)

        pixmap_tela_vitoria = QPixmap("./must_earn_TelaDaVitoria.jpeg")
        pixmap_tela_vitoria = pixmap_tela_vitoria.scaled(
            650,
            480,
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )

        self.tela_vitoria_img.setPixmap(pixmap_tela_vitoria)
        self.tela_vitoria_img.setAlignment(Qt.AlignCenter)

        vbox.addWidget(self.tela_vitoria_img)


        self.botao_restart.setFixedSize(300, 80)
        self.botao_restart.setCursor(Qt.PointingHandCursor)

        vbox.addWidget(self.botao_restart, alignment=Qt.AlignCenter)


        self.botao_sair.setFixedSize(300, 80)
        self.botao_sair.setCursor(Qt.PointingHandCursor)

        vbox.addWidget(self.botao_sair, alignment=Qt.AlignCenter)


        self.setLayout(vbox)


        self.botao_restart.clicked.connect(self.restart)
        self.botao_sair.clicked.connect(self.sair_do_jogo)



    def restart(self): # RESETA OS STATUS DO PLAYER, FECHA A JANELA PRINCIPAL E REABRE A JANELA DE LOGIN
        player.reset()
        self.login = Login()
        self.login.show()
        self.must_earn.close()
        self.accept()


    def sair_do_jogo(self): # FECHA O JOGO
        QApplication.quit()


class MustEarn(QWidget):
    def __init__(self):
        super().__init__()

        # CRIA A LISTA DOS CENARIOS, VALIDAÇÃO E A LOJA QUE SERA USADA NO CODIGO
        self.lista_cenarios = [1, 2, 3, 4, 5, 6, 7, 8]
        self.validacao = True

        self.loja = None


        # CRIACAO DOS BOTOES, TEXTOS, INPUTS, ETC
        self.titulo = QLabel("MUST EARN")

        self.username = QLabel(f"Nome: {player.nome}")


        self.comida = QLabel(f"Comida: {player.comida}/{str(player.max_comida)}", self)
        self.remedio = QLabel(f"Remédio: {player.remedio}/{str(player.max_remedio)}", self)
        self.aluguel = QLabel(f"Aluguel: {player.aluguel}/{str(player.max_aluguel)}", self)
        self.saldo = QLabel(f"Saldo: R${player.dinheiro:.2f}", self)


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
        #CRIACAO DO LAYOUT DA INTERFACE
        self.setWindowTitle("MUST EARN")
        self.setFixedSize(900, 850)

        self.setStyleSheet("""
QWidget {
    background-color: #020406;
    color: #2DE2E6;
    font-family: Consolas;
}

QLabel {
    color: #2DE2E6;
    font-weight: bold;
}

QLineEdit {
    background-color: #071014;
    color: #39FF88;
    border: 2px solid #2DE2E6;
    border-radius: 8px;
    padding: 5px;
}

QTextEdit {
    background-color: #071014;
    color: #D6F5FF;
    border: 2px solid #2DE2E6;
    border-radius: 8px;
}

QPushButton {
    background-color: #071014;
    color: #39FF88;
    border: 2px solid #39FF88;
    border-radius: 10px;
    padding: 10px;
    font-weight: bold;
}

QPushButton:hover {
    background-color: #39FF88;
    color: black;
}

QPushButton:pressed {
    background-color: #2DE2E6;
    color: black;
}
""")

        vbox = QVBoxLayout()


        pixmap_titulo = QPixmap("./must_earn_logo_2.png")
        pixmap_titulo = pixmap_titulo.scaled(
            260,
            120,
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation   
        )
        self.titulo.setPixmap(pixmap_titulo)
        self.titulo.setAlignment(Qt.AlignCenter)
        self.titulo.setStyleSheet("""
            background: transparent;
            border: none;
            padding: 0px;
            margin: 0px;
        """)

        vbox.addWidget(self.titulo)


        vbox.addWidget(self.username)


        hbox_status = QHBoxLayout()
        hbox_status.addWidget(self.comida)
        hbox_status.addWidget(self.remedio)
        hbox_status.addWidget(self.aluguel)
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


        #ESSA LISTA PEGA OS INPUTS DAS ACOES E JUNTA EM LISTA PARA NAO TER Q CHAMAR UM POR UM
        self.acoes_valores = [self.acao_1, self.acao_2, self.acao_3,
                              self.acao_4, self.acao_5, self.acao_6,
                              self.acao_7, self.acao_8, self.acao_9]

        self.mostrar_cenario()

        #QUANDO CLICA O BOTAO RODA ESSA LINHA QUE CHAMA A FUNCAO INICIALIZAR_DADOS_ACOES()
        self.botao_jogar.clicked.connect(self.inicializar_dados_acoes)
        self.botao_loja.clicked.connect(self.abrir_loja)


    def get_valores_investidos(self, acoes_valores: list):
        self.validacao = True
        valores = [] #LISTA COM O VALOR DO INVESTIMENTO, EM ORDEM
        dinheiro_aplicado = 0

        for acao in acoes_valores:
            try:
                if acao.text() == "": # TENTA PUXAR O VALOR DO INPUT E CASO DE ERRO RESOLVE
                    valor = float(acao.placeholderText())
                    valores.append(valor)
                else:
                    valor = float(acao.text())
                    valores.append(valor)
                    dinheiro_aplicado += valor
            except ValueError:
                self.jornal.append("--Os valores investidos devem ser um número--")
                acao.clear()
                self.validacao = False
                return None

        if player.aplicar_dinheiro(dinheiro_aplicado):
            self.saldo.setText(f"Saldo: R${str(round(player.dinheiro, 2))}")
        else:
            self.jornal.append("Saldo Insuficiente")
            self.validacao = False
            return None


        #DICIONARIO DO KAUE Q VAI SER RETORNADO, COM OS VALORES DOS INVESTIMENTOS
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

        # --- Processamento ---
        # 1. Aplica o cálculo matemático no dicionário
        dicionario_ativos_investimentos_iniciais = dicionario_ativos.copy()
        dicionario_atualizado = acoesv2.aplicar_cenario(self.cenario_sorteado, dicionario_ativos)


        lucro_rodada = player.resultado_investimentos(dicionario_ativos_investimentos_iniciais, dicionario_atualizado)
        self.saldo.setText(f"Saldo: R${str(round(player.dinheiro, 2))}")


        # --- Outputs Formatados no Terminal ---
        self.jornal.append("VALOR ATUALIZADO DOS ATIVOS POST-PREGÃO:")
        self.jornal.append("=" * 30)
        for ativo, valor in dicionario_atualizado.items():
            self.jornal.append(f"{ativo}: {valor:.4f}")
        self.jornal.append("=" * 30)
        self.jornal.append(f"Lucro dos Investimentos: R${lucro_rodada:.2f}")

        player.diminuir_comida()
        player.diminuir_remedio()
        player.diminuir_aluguel()

        self.atualizar_status()

        self.gastos_diarios = GastosDiarios()
        self.gastos_diarios.exec_()

        player.aumentar_rodada()

        self.jornal.append("Fim do Dia! Você recebe sua diária de R$1000.00")
        player.receber_dinheiro(1000)


        self.atualizar_status()

        self.checar_status()

        self.limpar_investimentos()

        # Função que chama o histórico na main (Não consegui testar)
        #historico.registrar_dia(player)

        self.mostrar_cenario()


    def mostrar_cenario(self): # FUNCAO PARA MOSTRAR O TEXTO E SETAR O CENARIO PARA A RODADA
        escolha_cenario = random.choice(self.lista_cenarios)
        cenario_sorteado = self.lista_cenarios.index(escolha_cenario) + 1

        # 2. Puxa o texto correspondente do arquivo textos.py usando o id do cenário
        texto_do_cenario = random.choice(textos.cenarios[cenario_sorteado])
        print(random.choice(textos.cenarios[cenario_sorteado]))

        # MOSTRA O CENARIO NO JORNAL
        self.jornal.append("=" * 30)
        self.jornal.append("NOTÍCIA DO CENÁRIO SORTEADO")
        self.jornal.append("=" * 30)
        self.jornal.append(texto_do_cenario)
        self.jornal.append("\n" + "=" * 30)

        self.cenario_sorteado = cenario_sorteado
        return


    def atualizar_status(self): # FUNCAO PARA ATUALIZAR OS DADOS TODA RODADA
        self.comida.setText(f"Comida: {str(player.comida)}/{str(player.max_comida)}")
        self.remedio.setText(f"Remédio: {str(player.remedio)}/{str(player.max_remedio)}")
        self.aluguel.setText(f"Aluguel: {str(player.aluguel)}/{str(player.max_aluguel)}")
        self.saldo.setText(f"Saldo: R${str(round(player.dinheiro, 2))}")

    def abrir_loja(self): #ABRE A LOJA DE POWERUPS
        self.loja = powerups.Loja(player)
        self.loja.exec_()
        self.atualizar_status()
        self.checar_status()


    def checar_status(self): #AO FINAL DE TODA RODADA CHECA OS STATUS
        # 1. CHECA SE OS STATUS ESTAO ZERADOS, SE SIM PERDE O JOGO E ABRE TELA DE GAME OVER
        if player.comida == 0 or player.aluguel == 0 or player.remedio == 0:
            Histórico.gerar_relatorio(player.nome, player.rodadas, player.lucro_total_partida, False)
            self.game_over = GameOver(self)
            self.game_over.exec_()
            self.close()
        else: # CHECA SE O PLAYER COMPROU TODOS OS UPGRADES, SE SIM GANHA O JOGO E ABRE TELA DE VITORIA
            if self.loja and self.loja.checar_comprados():
                Histórico.gerar_relatorio(player.nome, player.rodadas, player.lucro_total_partida, True)
                self.tela_vitoria = TelaDaVitoria(self)
                self.tela_vitoria.exec_()
                self.close()

    
    def limpar_investimentos(self): # AO FIM DA RODADA LIMPA OS INVESTIMENTOS ANTERIORES
        for acao in self.acoes_valores:
            acao.setPlaceholderText("0.00")
        


player = Player()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = Login()
    login.show()
    sys.exit(app.exec_())
