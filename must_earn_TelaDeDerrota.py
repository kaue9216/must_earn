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

class TelaDeDerrota(QWidget):
    def __init__(self):
        super().__init__()


        self.setWindowTitle("MUST EARN")
        self.setFixedSize(900, 850)

        #Layout
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