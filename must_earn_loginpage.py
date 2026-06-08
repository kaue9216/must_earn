import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QLineEdit,
    QVBoxLayout
)

from PyQt5.QtGui import  QPixmap
from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QGraphicsDropShadowEffect
from PyQt5.QtGui import QColor


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
        color: #2DE2E6;
        font-size: 56px;
        font-weight: 900;
        margin-top: 30px;
        letter-spacing: 4px;
        """)

        sombra = QGraphicsDropShadowEffect()
        sombra.setBlurRadius(35)
        sombra.setOffset(0)
        sombra.setColor(QColor("#2DE2E6"))

        titulo.setGraphicsEffect(sombra)

        layout.addWidget(titulo)

        # Imagem
        imagem = QLabel()

        pixmap = QPixmap("./must_earn.jpeg")

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

        texto.setStyleSheet("""
    color: #39FF88;
    font-size: 20px;
    font-weight: bold;
""")

        self.usuario.setStyleSheet("""
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

        self.botao.setStyleSheet("""
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

        self.setStyleSheet("""
    QWidget {
        background-color: #020406;
        color: #2DE2E6;
        font-family: Consolas;
    }
""")

        self.setLayout(layout)


# Executar a tela de login
app = QApplication(sys.argv)

window = MustEarn()
window.show()

sys.exit(app.exec_())
