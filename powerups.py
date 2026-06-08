from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QDialog, QScrollArea
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class MacacoDigital:
    def __init__(self, player):
        self.comprado = False
        self.player = player

    def comprar(self):
        self.comprado = self.player.comprar_item(50000)
        return self.comprado

class Alianca:
    def __init__(self, player):
        self.comprado = False
        self.player = player

    def comprar(self):
        self.comprado = self.player.comprar_item(50000)
        return self.comprado

class Kitnet:
    def __init__(self, player):
        self.comprado = False
        self.player = player

    def comprar(self):
        self.comprado = self.player.comprar_item(25000)
        if self.comprado:
            self.player.diminuir_preco_aluguel(100)
            return self.comprado
        return self.comprado

class Galinha:
    def __init__(self, player):
        self.comprado = False
        self.player = player

    def comprar(self):
        self.comprado = self.player.comprar_item(25000)
        if self.comprado:
            self.player.diminuir_preco_comida(100)
            return self.comprado
        return self.comprado

class OutraGalinha:
    def __init__(self, player):
        self.comprado = False
        self.player = player

    def comprar(self):
        self.comprado = self.player.comprar_item(25000)
        if self.comprado:
            self.player.diminuir_preco_comida(100)
            self.player.aumentar_max_comida(1)
            return self.comprado
        return self.comprado

class HorarioDeAlmoco:
    def __init__(self, player):
        self.comprado = False
        self.player = player

    def comprar(self):
        self.comprado = self.player.comprar_item(2000)
        if self.comprado:
            self.player.aumentar_max_comida(1)
            return self.comprado
        return self.comprado

class ColetePuffer:
    def __init__(self, player):
        self.comprado = False
        self.player = player

    def comprar(self):
        self.comprado = self.player.comprar_item(6000)
        if self.comprado:
            self.player.aumentar_max_comida(1)
            self.player.aumentar_max_aluguel(1)
            self.player.aumentar_max_remedio(1)
            return self.comprado
        return self.comprado

class GeladeiraPremium:
    def __init__(self, player):
        self.comprado = False
        self.player = player

    def comprar(self):
        self.comprado = self.player.comprar_item(2000)
        if self.comprado:
            self.player.diminuir_preco_comida(50)
            return self.comprado
        return self.comprado

class Cruz:
    def __init__(self, player):
        self.comprado = False
        self.player = player

    def comprar(self):
        self.comprado = self.player.comprar_item(7500)
        if self.comprado:
            self.player.aumentar_max_aluguel(1)
            self.player.aumentar_max_comida(1)
            self.player.aumentar_max_remedio(1)
            return self.comprado
        return self.comprado

class CarroEsportivo:
    def __init__(self, player):
        self.comprado = False
        self.player = player

    def comprar(self):
        self.comprado = self.player.comprar_item(100000)
        return self.comprado

class FaturamentoAbsurdo:
    def __init__(self, player):
        self.comprado = False
        self.player = player

    def comprar(self):
        self.comprado = self.player.comprar_item(2000)
        if self.comprado:
            self.player.aumentar_max_comida(1)
            return self.comprado
        return self.comprado

class CasaPropia:
    def __init__(self, player):
        self.comprado = False
        self.player = player

    def comprar(self):
        self.comprado = self.player.comprar_item(50000)
        if self.comprado:
            self.player.aumentar_max_aluguel(999)
            return self.comprado
        return self.comprado

class Omega3:
    def __init__(self, player):
        self.comprado = False
        self.player = player

    def comprar(self):
        self.comprado = self.player.comprar_item(2000)
        if self.comprado:
            self.player.aumentar_max_remedio(1)
            return self.comprado
        return self.comprado

class Sus:
    def __init__(self, player):
        self.comprado = False
        self.player = player

    def comprar(self):
        self.comprado = self.player.comprar_item(25000)
        if self.comprado:
            self.player.aumentar_max_remedio(999)
            return self.comprado
        return self.comprado

class PromocaoTrabalho:
    def __init__(self, player):
        self.comprado = False
        self.player = player

    def comprar(self):
        self.comprado = self.player.comprar_item(4000)
        if self.comprado:
            self.player.diminuir_preco_remedio(150)
            self.player.diminuir_preco_comida(50)
            return self.comprado
        return self.comprado

class Folga:
    def __init__(self, player):
        self.comprado = False
        self.player = player

    def comprar(self):
        self.comprado = self.player.comprar_item(2000)
        if self.comprado:
            self.player.aumentar_max_remedio(1)
            return self.comprado
        return self.comprado

class ParteBoaCidade:
    def __init__(self, player):
        self.comprado = False
        self.player = player

    def comprar(self):
        self.comprado = self.player.comprar_item(2000)
        if self.comprado:
            self.player.aumentar_max_aluguel(1)
            self.player.diminuir_preco_aluguel(50)
            return self.comprado
        return self.comprado

class Videogame:
    def __init__(self, player):
        self.comprado = False
        self.player = player

    def comprar(self):
        self.comprado = self.player.comprar_item(1500)
        return self.comprado


class Loja(QDialog):
    def __init__(self, player):
        super().__init__()

        self.player = player

        self.macaco_digital = MacacoDigital(player)
        self.alianca = Alianca(player)
        self.kitnet = Kitnet(player)
        self.galinha = Galinha(player)
        self.outra_galinha = OutraGalinha(player)
        self.horario_almoco = HorarioDeAlmoco(player)
        self.colete_puffer = ColetePuffer(player)
        self.geladeira_premium = GeladeiraPremium(player)
        self.cruz = Cruz(player)
        self.carro_esportivo = CarroEsportivo(player)
        self.faturamento_absurdo = FaturamentoAbsurdo(player)
        self.casa_propria = CasaPropia(player)
        self.omega_3 = Omega3(player)
        self.sus = Sus(player)
        self.promocao_trabalho = PromocaoTrabalho(player)
        self.folga = Folga(player)
        self.parte_boa_cidade = ParteBoaCidade(player)
        self.videogame = Videogame(player)

        self.upgrades: list = [self.macaco_digital, self.alianca, self.kitnet,
                               self.galinha, self.outra_galinha, self.horario_almoco,
                               self.colete_puffer, self.geladeira_premium, self.cruz,
                               self.carro_esportivo, self.faturamento_absurdo, self.casa_propria,
                               self.omega_3, self.sus, self.promocao_trabalho, self.folga,
                               self.parte_boa_cidade, self.videogame]

        self.titulo = QLabel("MERCADO DE UPGRADES")
        self.saldo = QLabel(f"Saldo: R${self.player.dinheiro:.2f}")
        
        self.macaco_digital_titulo = QLabel("Macaco Digital")
        self.macaco_digital_descricao = QLabel("Esse íem não faz nada, mas seus amigos saberão que você tem dinheiro para compra-lo")
        self.macaco_digital_img = QLabel()
        self.macaco_digital_botao = QPushButton("Comprar R$50.000")

        self.alianca_titulo = QLabel("Aliança")
        self.alianca_descricao = QLabel("Agora você tem uma namorada, só não vai me aparecer com um filho pra não sair da empresa")
        self.alianca_img = QLabel()
        self.alianca_botao = QPushButton("Comprar R$50.000")

        self.kitnet_titulo = QLabel("Kitnet")
        self.kitnet_descricao = QLabel("Talvez um apartamento de 6m² não seja o mais espaçoso, mas pelo menos vai te economizar no aluguel ")
        self.kitnet_img = QLabel()
        self.kitnet_botao = QPushButton("Comprar R$25.000")

        self.galinha_titulo = QLabel("Galinha")
        self.galinha_descricao = QLabel("Ela faz tudo que uma galinha faz")
        self.galinha_img = QLabel()
        self.galinha_botao = QPushButton("Comprar R$25.000")

        self.outra_galinha_titulo = QLabel("Outra Galinha")
        self.outra_galinha_descricao = QLabel("Essa também faz tudo qo que uma galinha faz")
        self.outra_galinha_img = QLabel()
        self.outra_galinha_botao = QPushButton("Comprar R$25.000")

        self.horario_almoco_titulo = QLabel("Horário de Almoço")
        self.horario_almoco_descricao = QLabel("Você negociou com o patrão direitinho, agora tem 15 minutos pra comer durante o dia, use com sabedoria")
        self.horario_almoco_img = QLabel()
        self.horario_almoco_botao = QPushButton("Comprar R$2000")
        
        self.colete_puffer_titulo = QLabel("Colete Puffer")
        self.colete_puffer_descricao = QLabel("Esse ítem lendário te coloca cada vez mais perto da liberdade financeira")
        self.colete_puffer_img = QLabel()
        self.colete_puffer_botao = QPushButton("Comprar R$6000")

        self.geladeira_premium_titulo = QLabel("Geladeira Premium")
        self.geladeira_premium_descricao = QLabel("Agora você nâo precisa mais aguardar o final dos anúncios para abrir a sua geladeira")
        self.geladeira_premium_img = QLabel()
        self.geladeira_premium_botao = QPushButton("Comprar R$2000")

        self.cruz_titulo = QLabel("Cruz")
        self.cruz_descricao = QLabel("Todos precisam de uma segunda chance")
        self.cruz_img = QLabel()
        self.cruz_botao = QPushButton("Comprar R$7500")

        self.carro_esportivo_titulo = QLabel("Carro Esportivo")
        self.carro_esportivo_descricao = QLabel("Agora você tem o carro da moda, mas o transito na merginal continua o mesmo")
        self.carro_esportivo_img = QLabel()
        self.carro_esportivo_botao = QPushButton("Comprar R$100.000")

        self.faturamento_absurdo_titulo = QLabel("Faturamento Absurdo")
        self.faturamento_absurdo_descricao = QLabel("A empresa bateu record de faturamento, você ganhou um copo de suco de laranja")
        self.faturamento_absurdo_img = QLabel()
        self.faturamento_absurdo_botao = QPushButton("Comprar R$2000")

        self.casa_propria_titulo = QLabel("Casa Própria")
        self.casa_propria_descricao = QLabel("Nesse mundo rotativo você foi o unico a decidir comprar uma casa própria, seja feliz")
        self.casa_propria_img = QLabel()
        self.casa_propria_botao = QPushButton("Comprar R$50.000")

        self.omega_3_titulo = QLabel("Omega 3")
        self.omega_3_descricao = QLabel("Dizem que depois dessa compra, sua saúde fica 'Top'")
        self.omega_3_img = QLabel()
        self.omega_3_botao = QPushButton("Comprar R$2000")

        self.sus_titulo = QLabel("SUS")
        self.sus_descricao = QLabel("Compre e ganhe atendimento médico grátis pra sempre, de qualidade duvidosa")
        self.sus_img = QLabel()
        self.sus_botao = QPushButton("Comprar R$25.000")

        self.promocao_trabalho_titulo = QLabel("Promoçao no Trabalho")
        self.promocao_trabalho_descricao = QLabel("Como você trabalha incansavélmente e não tem problema em ficar 'um pouquinho' até mais tarde, seu patrão vai te recompansar a altura. Você ganhou o direito de utilizar uma gaveta no seu trabalho")
        self.promocao_trabalho_img = QLabel()
        self.promocao_trabalho_botao = QPushButton("Comprar R$4000")

        self.folga_titulo = QLabel("Folga")
        self.folga_descricao = QLabel("Seu patrão não gostou muito, mas concordou com um dia de folga. Agora você trabalha na tão sonhada 13X1")
        self.folga_img = QLabel()
        self.folga_botao = QPushButton("Comprar R$2000")

        self.parte_boa_cidade_titulo = QLabel("Parte Boa da Cidade")
        self.parte_boa_cidade_descricao = QLabel("O seu novo apartamento  não é exatamente perto do trabalho, mas pelo menos você acostuma com o constante som de alarmes e janelas quebrando")
        self.parte_boa_cidade_img = QLabel()
        self.parte_boa_cidade_botao = QPushButton("Comprar R$2000")

        self.videogame_titulo = QLabel("Videogame")
        self.videogame_descricao = QLabel("HAHAHA! Até parece que vai ter tempo pra jogar")
        self.videogame_img = QLabel()
        self.videogame_botao = QPushButton("Comprar R$1500")

        self.botao_fechar = QPushButton("Fechar")

        self.initUi()


    def initUi(self):
        self.setWindowTitle("MUST EARN")
        self.setFixedSize(950, 850)

        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        main_layout.addWidget(self.titulo)
        main_layout.addWidget(self.saldo)


        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        main_layout.addWidget(scroll)

        conteudo = QWidget()
        scroll.setWidget(conteudo)

        vbox = QVBoxLayout()
        conteudo.setLayout(vbox)

        # MACACO DIGITAL
        hbox_macaco_digital = QHBoxLayout()
        hbox_macaco_digital.addWidget(self.macaco_digital_img)
        macaco_digital_pixmap = QPixmap("./must_earn_macaco_digital.jpeg")
        macaco_digital_pixmap = macaco_digital_pixmap.scaled(
            200,
            200,
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )
        self.macaco_digital_img.setPixmap(macaco_digital_pixmap)
        vbox_macaco_digital = QVBoxLayout()
        vbox_macaco_digital.addWidget(self.macaco_digital_titulo)
        vbox_macaco_digital.addWidget(self.macaco_digital_descricao)
        vbox_macaco_digital.addWidget(self.macaco_digital_botao)
        hbox_macaco_digital.addLayout(vbox_macaco_digital)
        vbox.addLayout(hbox_macaco_digital)

        # ALIANCA
        hbox_alianca = QHBoxLayout()
        hbox_alianca.addWidget(self.alianca_img)
        alianca_pixmap = QPixmap("./must_earn_alianca.jpeg")
        alianca_pixmap = alianca_pixmap.scaled(
            200,
            200,
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )
        self.alianca_img.setPixmap(alianca_pixmap)
        vbox_alianca = QVBoxLayout()
        vbox_alianca.addWidget(self.alianca_titulo)
        vbox_alianca.addWidget(self.alianca_descricao)
        vbox_alianca.addWidget(self.alianca_botao)
        hbox_alianca.addLayout(vbox_alianca)
        vbox.addLayout(hbox_alianca)

        # KITNET
        hbox_kitnet = QHBoxLayout()
        hbox_kitnet.addWidget(self.kitnet_img)
        kitnet_pixmap = QPixmap("./must_earn_kitnet.jpeg")
        kitnet_pixmap = kitnet_pixmap.scaled(
            200,
            200,
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )
        self.kitnet_img.setPixmap(kitnet_pixmap)
        vbox_kitnet = QVBoxLayout()
        vbox_kitnet.addWidget(self.kitnet_titulo)
        vbox_kitnet.addWidget(self.kitnet_descricao)
        vbox_kitnet.addWidget(self.kitnet_botao)
        hbox_kitnet.addLayout(vbox_kitnet)
        vbox.addLayout(hbox_kitnet)

        # GALINHA
        hbox_galinha = QHBoxLayout()
        hbox_galinha.addWidget(self.galinha_img)
        galinha_pixmap = QPixmap("./must_earn_galinha.jpeg")
        galinha_pixmap = galinha_pixmap.scaled(
            200,
            200,
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )
        self.galinha_img.setPixmap(galinha_pixmap)
        vbox_galinha = QVBoxLayout()
        vbox_galinha.addWidget(self.galinha_titulo)
        vbox_galinha.addWidget(self.galinha_descricao)
        vbox_galinha.addWidget(self.galinha_botao)
        hbox_galinha.addLayout(vbox_galinha)
        vbox.addLayout(hbox_galinha)

        # OUTRA GALINHA
        hbox_outra_galinha = QHBoxLayout()
        hbox_outra_galinha.addWidget(self.outra_galinha_img)
        outra_galinha_pixmap = QPixmap("./must_earn_outra_galinha.jpeg")
        outra_galinha_pixmap = outra_galinha_pixmap.scaled(
            200,
            200,
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )
        self.outra_galinha_img.setPixmap(outra_galinha_pixmap)
        vbox_outra_galinha = QVBoxLayout()
        vbox_outra_galinha.addWidget(self.outra_galinha_titulo)
        vbox_outra_galinha.addWidget(self.outra_galinha_descricao)
        vbox_outra_galinha.addWidget(self.outra_galinha_botao)
        hbox_outra_galinha.addLayout(vbox_outra_galinha)
        vbox.addLayout(hbox_outra_galinha)

        # HORARIO DE ALMOCO
        hbox_horario_almoco = QHBoxLayout()
        hbox_horario_almoco.addWidget(self.horario_almoco_img)
        horario_almoco_pixmap = QPixmap("./must_earn_horario_almoco.jpeg")
        horario_almoco_pixmap = horario_almoco_pixmap.scaled(
            200,
            200,
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )
        self.horario_almoco_img.setPixmap(horario_almoco_pixmap)
        vbox_horario_almoco = QVBoxLayout()
        vbox_horario_almoco.addWidget(self.horario_almoco_titulo)
        vbox_horario_almoco.addWidget(self.horario_almoco_descricao)
        vbox_horario_almoco.addWidget(self.horario_almoco_botao)
        hbox_horario_almoco.addLayout(vbox_horario_almoco)
        vbox.addLayout(hbox_horario_almoco)

        # COLETE PUFFER
        hbox_colete_puffer = QHBoxLayout()
        hbox_colete_puffer.addWidget(self.colete_puffer_img)
        colete_puffer_pixmap = QPixmap("./must_earn_colete_puffer.jpeg")
        colete_puffer_pixmap = colete_puffer_pixmap.scaled(
            200,
            200,
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )
        self.colete_puffer_img.setPixmap(colete_puffer_pixmap)
        vbox_colete_puffer = QVBoxLayout()
        vbox_colete_puffer.addWidget(self.colete_puffer_titulo)
        vbox_colete_puffer.addWidget(self.colete_puffer_descricao)
        vbox_colete_puffer.addWidget(self.colete_puffer_botao)
        hbox_colete_puffer.addLayout(vbox_colete_puffer)
        vbox.addLayout(hbox_colete_puffer)

        # GELADEIRA PREMIUM
        hbox_geladeira_premium = QHBoxLayout()
        hbox_geladeira_premium.addWidget(self.geladeira_premium_img)
        geladeira_premium_pixmap = QPixmap("./must_earn_geladeira_premium.jpeg")
        geladeira_premium_pixmap = geladeira_premium_pixmap.scaled(
            200,
            200,
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )
        self.geladeira_premium_img.setPixmap(geladeira_premium_pixmap)
        vbox_geladeira_premium = QVBoxLayout()
        vbox_geladeira_premium.addWidget(self.geladeira_premium_titulo)
        vbox_geladeira_premium.addWidget(self.geladeira_premium_descricao)
        vbox_geladeira_premium.addWidget(self.geladeira_premium_botao)
        hbox_geladeira_premium.addLayout(vbox_geladeira_premium)
        vbox.addLayout(hbox_geladeira_premium)

        # CRUZ
        hbox_cruz = QHBoxLayout()
        hbox_cruz.addWidget(self.cruz_img)
        cruz_pixmap = QPixmap("./must_earn_cruz.jpeg")
        cruz_pixmap = cruz_pixmap.scaled(
            200,
            200,
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )
        self.cruz_img.setPixmap(cruz_pixmap)
        vbox_cruz = QVBoxLayout()
        vbox_cruz.addWidget(self.cruz_titulo)
        vbox_cruz.addWidget(self.cruz_descricao)
        vbox_cruz.addWidget(self.cruz_botao)
        hbox_cruz.addLayout(vbox_cruz)
        vbox.addLayout(hbox_cruz)

        # CARRO ESPORTIVO
        hbox_carro_esportivo = QHBoxLayout()
        hbox_carro_esportivo.addWidget(self.carro_esportivo_img)
        carro_esportivo_pixmap = QPixmap("./must_earn_carro_esportivo.jpeg")
        carro_esportivo_pixmap = carro_esportivo_pixmap.scaled(
            200,
            200,
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )
        self.carro_esportivo_img.setPixmap(carro_esportivo_pixmap)
        vbox_carro_esportivo = QVBoxLayout()
        vbox_carro_esportivo.addWidget(self.carro_esportivo_titulo)
        vbox_carro_esportivo.addWidget(self.carro_esportivo_descricao)
        vbox_carro_esportivo.addWidget(self.carro_esportivo_botao)
        hbox_carro_esportivo.addLayout(vbox_carro_esportivo)
        vbox.addLayout(hbox_carro_esportivo)

        # FATURAMENTO ABSURDO
        hbox_faturamento_absurdo = QHBoxLayout()
        hbox_faturamento_absurdo.addWidget(self.faturamento_absurdo_img)
        faturamento_absurdo_pixmap = QPixmap("./must_earn_faturamento_absurdo.jpeg")
        faturamento_absurdo_pixmap = faturamento_absurdo_pixmap.scaled(
            200,
            200,
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )
        self.faturamento_absurdo_img.setPixmap(faturamento_absurdo_pixmap)
        vbox_faturamento_absurdo = QVBoxLayout()
        vbox_faturamento_absurdo.addWidget(self.faturamento_absurdo_titulo)
        vbox_faturamento_absurdo.addWidget(self.faturamento_absurdo_descricao)
        vbox_faturamento_absurdo.addWidget(self.faturamento_absurdo_botao)
        hbox_faturamento_absurdo.addLayout(vbox_faturamento_absurdo)
        vbox.addLayout(hbox_faturamento_absurdo)

        # CASA PROPRIA
        hbox_casa_propria = QHBoxLayout()
        hbox_casa_propria.addWidget(self.casa_propria_img)
        casa_propria_pixmap = QPixmap("./must_earn_casa_propria.jpeg")
        casa_propria_pixmap = casa_propria_pixmap.scaled(
            200,
            200,
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )
        self.casa_propria_img.setPixmap(casa_propria_pixmap)
        vbox_casa_propria = QVBoxLayout()
        vbox_casa_propria.addWidget(self.casa_propria_titulo)
        vbox_casa_propria.addWidget(self.casa_propria_descricao)
        vbox_casa_propria.addWidget(self.casa_propria_botao)
        hbox_casa_propria.addLayout(vbox_casa_propria)
        vbox.addLayout(hbox_casa_propria)

        # OMEGA 3
        hbox_omega_3 = QHBoxLayout()
        hbox_omega_3.addWidget(self.omega_3_img)
        omega_3_pixmap = QPixmap("./must_earn_omega_3.jpeg")
        omega_3_pixmap = omega_3_pixmap.scaled(
            200,
            200,
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )
        self.omega_3_img.setPixmap(omega_3_pixmap)
        vbox_omega_3 = QVBoxLayout()
        vbox_omega_3.addWidget(self.omega_3_titulo)
        vbox_omega_3.addWidget(self.omega_3_descricao)
        vbox_omega_3.addWidget(self.omega_3_botao)
        hbox_omega_3.addLayout(vbox_omega_3)
        vbox.addLayout(hbox_omega_3)

        # SUS
        hbox_sus = QHBoxLayout()
        hbox_sus.addWidget(self.sus_img)
        sus_pixmap = QPixmap("./must_earn_sus.jpeg")
        sus_pixmap = sus_pixmap.scaled(
            200,
            200,
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )
        self.sus_img.setPixmap(sus_pixmap)
        vbox_sus = QVBoxLayout()
        vbox_sus.addWidget(self.sus_titulo)
        vbox_sus.addWidget(self.sus_descricao)
        vbox_sus.addWidget(self.sus_botao)
        hbox_sus.addLayout(vbox_sus)
        vbox.addLayout(hbox_sus)

        # PROMOCAO TRABALHO
        hbox_promocao_trabalho = QHBoxLayout()
        hbox_promocao_trabalho.addWidget(self.promocao_trabalho_img)
        promocao_trabalho_pixmap = QPixmap("./must_earn_promocao_trabalho.jpeg")
        promocao_trabalho_pixmap = promocao_trabalho_pixmap.scaled(
            200,
            200,
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )
        self.promocao_trabalho_img.setPixmap(promocao_trabalho_pixmap)
        vbox_promocao_trabalho = QVBoxLayout()
        vbox_promocao_trabalho.addWidget(self.promocao_trabalho_titulo)
        vbox_promocao_trabalho.addWidget(self.promocao_trabalho_descricao)
        vbox_promocao_trabalho.addWidget(self.promocao_trabalho_botao)
        hbox_promocao_trabalho.addLayout(vbox_promocao_trabalho)
        vbox.addLayout(hbox_promocao_trabalho)

        # FOLGA
        hbox_folga = QHBoxLayout()
        hbox_folga.addWidget(self.folga_img)
        folga_pixmap = QPixmap("./must_earn_folga.jpeg")
        folga_pixmap = folga_pixmap.scaled(
            200,
            200,
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )
        self.folga_img.setPixmap(folga_pixmap)
        vbox_folga = QVBoxLayout()
        vbox_folga.addWidget(self.folga_titulo)
        vbox_folga.addWidget(self.folga_descricao)
        vbox_folga.addWidget(self.folga_botao)
        hbox_folga.addLayout(vbox_folga)
        vbox.addLayout(hbox_folga)

        # PARTE BOA DA CIDADE
        hbox_parte_boa_cidade = QHBoxLayout()
        hbox_parte_boa_cidade.addWidget(self.parte_boa_cidade_img)
        parte_boa_cidade_pixmap = QPixmap("./must_earn_parte_boa_cidade.jpeg")
        parte_boa_cidade_pixmap = parte_boa_cidade_pixmap.scaled(
            200,
            200,
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )
        self.parte_boa_cidade_img.setPixmap(parte_boa_cidade_pixmap)
        vbox_parte_boa_cidade = QVBoxLayout()
        vbox_parte_boa_cidade.addWidget(self.parte_boa_cidade_titulo)
        vbox_parte_boa_cidade.addWidget(self.parte_boa_cidade_descricao)
        vbox_parte_boa_cidade.addWidget(self.parte_boa_cidade_botao)
        hbox_parte_boa_cidade.addLayout(vbox_parte_boa_cidade)
        vbox.addLayout(hbox_parte_boa_cidade)

        # VIDEOGAME
        hbox_videogame = QHBoxLayout()
        hbox_videogame.addWidget(self.videogame_img)
        videogame_pixmap = QPixmap("./must_earn_videogame.jpeg")
        videogame_pixmap = videogame_pixmap.scaled(
            200,
            200,
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )
        self.videogame_img.setPixmap(videogame_pixmap)
        vbox_videogame = QVBoxLayout()
        vbox_videogame.addWidget(self.videogame_titulo)
        vbox_videogame.addWidget(self.videogame_descricao)
        vbox_videogame.addWidget(self.videogame_botao)
        hbox_videogame.addLayout(vbox_videogame)
        vbox.addLayout(hbox_videogame)


        self.macaco_digital_img.setFixedSize(200, 200)
        self.alianca_img.setFixedSize(200, 200)
        self.kitnet_img.setFixedSize(200, 200)
        self.galinha_img.setFixedSize(200, 200)
        self.outra_galinha_img.setFixedSize(200, 200)
        self.horario_almoco_img.setFixedSize(200, 200)
        self.colete_puffer_img.setFixedSize(200, 200)
        self.geladeira_premium_img.setFixedSize(200, 200)
        self.cruz_img.setFixedSize(200, 200)
        self.carro_esportivo_img.setFixedSize(200, 200)
        self.faturamento_absurdo_img.setFixedSize(200, 200)
        self.casa_propria_img.setFixedSize(200, 200)
        self.omega_3_img.setFixedSize(200, 200)
        self.sus_img.setFixedSize(200, 200)
        self.promocao_trabalho_img.setFixedSize(200, 200)
        self.folga_img.setFixedSize(200, 200)
        self.parte_boa_cidade_img.setFixedSize(200, 200)
        self.videogame_img.setFixedSize(200, 200)


        self.macaco_digital_descricao.setWordWrap(True)
        self.alianca_descricao.setWordWrap(True)
        self.kitnet_descricao.setWordWrap(True)
        self.galinha_descricao.setWordWrap(True)
        self.outra_galinha_descricao.setWordWrap(True)
        self.horario_almoco_descricao.setWordWrap(True)
        self.colete_puffer_descricao.setWordWrap(True)
        self.geladeira_premium_descricao.setWordWrap(True)
        self.cruz_descricao.setWordWrap(True)
        self.carro_esportivo_descricao.setWordWrap(True)
        self.faturamento_absurdo_descricao.setWordWrap(True)
        self.casa_propria_descricao.setWordWrap(True)
        self.omega_3_descricao.setWordWrap(True)
        self.sus_descricao.setWordWrap(True)
        self.promocao_trabalho_descricao.setWordWrap(True)
        self.folga_descricao.setWordWrap(True)
        self.parte_boa_cidade_descricao.setWordWrap(True)
        self.videogame_descricao.setWordWrap(True)


        main_layout.addWidget(self.botao_fechar)

        self.macaco_digital_botao.clicked.connect(lambda: self.comprar_upgrade(i_upgrade=0, botao=self.macaco_digital_botao))
        self.alianca_botao.clicked.connect(lambda: self.comprar_upgrade(i_upgrade=1, botao=self.alianca_botao))
        self.kitnet_botao.clicked.connect(lambda: self.comprar_upgrade(i_upgrade=2, botao=self.kitnet_botao))
        self.galinha_botao.clicked.connect(lambda: self.comprar_upgrade(i_upgrade=3, botao=self.galinha_botao))
        self.outra_galinha_botao.clicked.connect(lambda: self.comprar_upgrade(i_upgrade=4, botao=self.outra_galinha_botao))
        self.horario_almoco_botao.clicked.connect(lambda: self.comprar_upgrade(i_upgrade=5, botao=self.horario_almoco_botao))
        self.colete_puffer_botao.clicked.connect(lambda: self.comprar_upgrade(i_upgrade=6, botao=self.colete_puffer_botao))
        self.geladeira_premium_botao.clicked.connect(lambda: self.comprar_upgrade(i_upgrade=7, botao=self.geladeira_premium_botao))
        self.cruz_botao.clicked.connect(lambda: self.comprar_upgrade(i_upgrade=8, botao=self.cruz_botao))
        self.carro_esportivo_botao.clicked.connect(lambda: self.comprar_upgrade(i_upgrade=9, botao=self.carro_esportivo_botao))
        self.faturamento_absurdo_botao.clicked.connect(lambda: self.comprar_upgrade(i_upgrade=10, botao=self.faturamento_absurdo_botao))
        self.casa_propria_botao.clicked.connect(lambda: self.comprar_upgrade(i_upgrade=11, botao=self.casa_propria_botao))
        self.omega_3_botao.clicked.connect(lambda: self.comprar_upgrade(i_upgrade=12, botao=self.omega_3_botao))
        self.sus_botao.clicked.connect(lambda: self.comprar_upgrade(i_upgrade=13, botao=self.sus_botao))
        self.promocao_trabalho_botao.clicked.connect(lambda: self.comprar_upgrade(i_upgrade=14, botao=self.promocao_trabalho_botao))
        self.folga_botao.clicked.connect(lambda: self.comprar_upgrade(i_upgrade=15, botao=self.folga_botao))
        self.parte_boa_cidade_botao.clicked.connect(lambda: self.comprar_upgrade(i_upgrade=16, botao=self.parte_boa_cidade_botao))
        self.videogame_botao.clicked.connect(lambda: self.comprar_upgrade(i_upgrade=17, botao=self.videogame_botao))

        self.botao_fechar.clicked.connect(self.accept)
        

    def comprar_upgrade(self, i_upgrade, botao):
        upgrade = self.upgrades[i_upgrade]
        if upgrade.comprar():
            botao.setText("Comprado")
            botao.setEnabled(False)
        self.atualizar_saldo()

    def atualizar_saldo(self):
        self.saldo.setText(f"Saldo: R${self.player.dinheiro}")


    def checar_comprados(self):
        upg_comprados = 0
        for upgrade in self.upgrades:
            if upgrade.comprado:
                upg_comprados += 1
        if upg_comprados == len(self.upgrades):
            return True
        else:
            return False


