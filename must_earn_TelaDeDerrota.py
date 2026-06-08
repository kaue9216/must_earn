import sys
from PyQt5.QtWidgets import(
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout
)

from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGraphicsDropShadowEffect
from PyQt5.QtGui import QColor


class TelaDeDerrota(QWidget):
    def __init__(self):
        super().__init__()


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





        #Layout
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        layout.setSpacing(30)

        # Titulo
        titulo = QLabel("MUST EARN")
        titulo.setAlignment(Qt.AlignCenter)

        titulo = QLabel("MUST EARN")
        titulo.setAlignment(Qt.AlignCenter)

        titulo.setStyleSheet("""
color: #FF3131;
font-size: 56px;
font-weight: 900;
letter-spacing: 4px;
margin-top: 20px;
""")

        sombra = QGraphicsDropShadowEffect()
        sombra.setBlurRadius(35)
        sombra.setOffset(0)
        sombra.setColor(QColor("#FF3131"))

        titulo.setGraphicsEffect(sombra)   



        layout.addWidget(titulo)

        # Imagem
        imagem = QLabel()

        pixmap = QPixmap("./must_earn_TelaDeDerrota.jpeg")

        pixmap = pixmap.scaled(
            650,
            450,
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )

        imagem.setPixmap(pixmap)

        imagem.setAlignment(Qt.AlignCenter)

        layout.addWidget(imagem)

        # Botao Para Jogar de novo
        self.botao = QPushButton("JOGAR DE NOVO")

        self.botao.setFixedSize(300, 80)

        self.botao.setCursor(Qt.PointingHandCursor)


        layout.addWidget(self.botao, alignment=Qt.AlignCenter)

        self.setLayout(layout)


        # Botao Para Sair
        self.botao_sair = QPushButton("Sair")
        self.botao_sair.setFixedSize(300, 80)
        self.botao_sair.setCursor(Qt.PointingHandCursor)
        self.botao_sair.setCursor(Qt.PointingHandCursor)
        self.botao_sair.clicked.connect(QApplication.instance().quit)
        layout.addWidget(self.botao_sair, alignment=Qt.AlignCenter)

        self.setLayout(layout)

# Executar a tela de login
app = QApplication(sys.argv)

window = TelaDeDerrota()
window.show()

sys.exit(app.exec_())