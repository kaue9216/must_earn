from player import Player

player = Player()

class MacacoDigital:
    def __init__(self):
        self.comprado = False

    def comprar(self):
        player.receber_dinheiro(-50000)
        print(player.dinheiro)
        self.comprado = True

class Alianca:
    def __init__(self):
        self.comprado = False

    def comprar(self):
        player.receber_dinheiro(-150)
        print(player.dinheiro)
        self.comprado = True

class Kitnet:
    def __init__(self):
        self.comprado = False

    def comprar(self):
        player.receber_dinheiro(-25000)
        player.aumemtar_max_aluguel(1)
        self.comprado = True

class Galinha:
    def __init__(self):
        self.comprado = False

    def comprar(self):
        player.receber_dinheiro(-25000)
        player.aumentar_comida(1000000000000000)
        self.comprado = True

class OutraGalinha:
    def __init__(self):
        self.comprado = False

    def comprar(self):
        player.receber_dinheiro(-25000)
        player.aumentar_max_comida(1000000000000000)
        self.comprado = True

class HorarioDeAlmoco:
    def __init__(self):
        self.comprado = False

    def comprar(self):
        player.receber_dinheiro(-2000)
        player.aumentar_max_comida(1)
        self.comprado = True

class ColetePuffer:
    def __init__(self):
        self.comprado = False

    def comprar(self):
        player.receber_dinheiro(-6000)
        player.aumentar_max_comida(1)
        player.aumemtar_max_aluguel(1)
        player.aumentar_max_remedio(1)
        self.comprado = True

class GeladeiraPremium:
    def __init__(self):
        self.comprado = False

    def comprar(self):
        player.receber_dinheiro(-2000)
        player.aumentar_max_comida(1)
        self.comprado = True

class Cruz:
    def __init__(self):
        self.comprado = False

    def comprar(self):
        player.receber_dinheiro(-750)
        player.aumentar_aluguel(1)
        player.aumentar_comida(1)
        player.aumentar_remdio(1)
        self.comprado = True

class CarroEsportivo:
    def __init__(self):
        self.comprado = False

    def comprar(self):
        player.receber_dinheiro(-100000)
        self.comprado = True

class FaturamentoAbsurdo:
    def __init__(self):
        self.comprado = False

    def comprar(self):
        player.receber_dinheiro(-2000)
        player.aumentar_comida(1)
        self.comprado = True

class CasaPorpia:
    def __init__(self):
        self.comprado = False

    def comprar(self):
        player.receber_dinheiro(-25000)
        player.aumemtar_max_aluguel(1000000000000000)
        self.comprado = True

class Omega3:
    def __init__(self):
        self.comprado = False

    def comprar(self):
        player.receber_dinheiro(-2000)
        player.aumentar_max_remedio(1)
        self.comprado = True

class Sus:
    def __init__(self):
        self.comprado = False

    def comprar(self):
        player.receber_dinheiro(-25000)
        player.aumentar_max_remedio(100000000000000)
        self.comprado = True

class PromocaoTrabalho:
    def __init__(self):
        self.comprado = False

    def comprar(self):
        player.receber_dinheiro(-4000)
        player.aumentar_max_remedio(1)
        player.aumentar_max_comida(1)
        self.comprado = True

class Folga:
    def __init__(self):
        self.comprado = False

    def comprar(self):
        player.receber_dinheiro(-2000)
        player.aumentar_max_remedio(1)
        self.comprado = True

class ParteBoaCidade:
    def __init__(self):
        self.comprado = False

    def comprar(self):
        player.receber_dinheiro(-2000)
        player.aumemtar_max_aluguel(1)
        self.comprado = True

class Videogame:
    def __init__(self):
        self.comprado = False

    def comprar(self):
        player.receber_dinheiro(-1500)
        self.comprado = True
