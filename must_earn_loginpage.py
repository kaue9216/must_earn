import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QLineEdit,
    QVBoxLayout
)

from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt


class MustEarn(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("MUST EARN")
        self.setFixedSize(900, 850)




        # Layout
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        layout.setSpacing(30)

        # Titulo
        titulo = QLabel("MUST EARN")
        titulo.setAlignment(Qt.AlignCenter)

        titulo.setStyleSheet("""
            margin-top: 30px;
        """)

        layout.addWidget(titulo)

        # Imagem
        imagem = QLabel()

        pixmap = QPixmap("/Users/gabrieldudeck/Downloads/must_earn.jpeg")

        pixmap = pixmap.scaled(
            650,
            450,
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )

        imagem.setPixmap(pixmap)

        imagem.setAlignment(Qt.AlignCenter)

        layout.addWidget(imagem)

        # Texto 'Insira o nome de usuario'
        texto = QLabel("Insira o nome de usuário:")
        texto.setAlignment(Qt.AlignCenter)


        layout.addWidget(texto)

        # Caixa para colocar o nome de usario
        self.usuario = QLineEdit()

        self.usuario.setPlaceholderText("Usuário...")

        self.usuario.setFixedSize(500, 60)


        self.usuario.setStyleSheet("""
            QLineEdit{
                padding-left: 20px;
            }
        """)

        layout.addWidget(self.usuario, alignment=Qt.AlignCenter)

        # Botao Jogar
        self.botao = QPushButton("JOGAR")

        self.botao.setFixedSize(300, 80)

        self.botao.setCursor(Qt.PointingHandCursor)


        layout.addWidget(self.botao, alignment=Qt.AlignCenter)

        self.setLayout(layout)


# Executar a tela de login
app = QApplication(sys.argv)

window = MustEarn()
window.show()

sys.exit(app.exec_())