# MODO ERRADO DEPENDENCY INVERSION PRINCIPLE, exemplo bem simples
from typing import Type


# Modulo de baixo nivel, nele é implementados os metodos especificos de cada veiculo
class Aviao:
    def voar(self, dado: any) -> None:
        print(f"{dado} está voando")


# Modulo de alto nivel, nesse caso ele depende das implementações do módulo de baixo nivel (Aviao)
# Quando for implementado mais veiculos, irá dar problema por causa da dependencia
class Veiculo:
    def __init__(self, tipo_veiculo: Type[Aviao]) -> None:
        self.tipo_veiculo = tipo_veiculo

    def voar(self, dado: any) -> None:
        self.tipo_veiculo.voar(dado)


veiculo = Veiculo(Aviao())
veiculo.voar('Aviao')
