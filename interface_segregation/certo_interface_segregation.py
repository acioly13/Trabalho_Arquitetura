# MODO CERTO INTERFACE SEGREGATION PRINCIPLE, exemplo bem simples

# Criei uma classe para cada tipo de veículo, ela implementa apenas os metodos que utiliza
class Aviao:
    def __init__(self, voar):
        self.voar = voar

    def voar(self):
        pass


# Criei uma classe para cada tipo de veículo, ela implementa apenas os metodos que utiliza
class Carro:
    def __init__(self, andar):
        self.andar = andar

    def andar(self):
        pass


# Criei uma classe para cada tipo de veículo, ela implementa apenas os metodos que utiliza
class Barco:
    def __init__(self, navegar):
        self.navegar = navegar

    def navegar(self):
        pass
