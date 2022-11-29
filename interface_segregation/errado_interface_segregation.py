# MODO ERRADO INTERFACE SEGREGATION PRINCIPLE, exemplo bem simples

"""
    Classe generica para todos os tipos de veículos, pode ser um problema ja que terão veiculos que não
    implementam todos os metodos
"""


class Veiculo:
    def __init__(self, voar, andar, navegar):
        self.voar = voar
        self.andar = andar
        self.navegar = navegar

    def voar(self):
        pass

    def andar(self):
        pass

    def navegar(self):
        pass



