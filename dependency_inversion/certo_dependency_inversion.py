# MODO CERTO DEPENDENCY INVERSION PRINCIPLE, exemplo bem simples
"""
    Módulos de alto nível: são as rotinas menos complexas e facéis de entender e visualizar
        não devem depender dos modulos de baixo nível e sim da abstração
    Módulos de baixo nível: são as rotinas mais complexas e difíceis de entender
        Geralmente são compostas de implementações de cálculos ou comportamentos específicos.
"""
from typing import Type
from abc import ABC, abstractmethod


# Interface que abstrai e define os metodos que o modulo de alto nivel irá utilizar
class TiposVeiculos(ABC):

    @abstractmethod
    def voar(self, dado: any) -> None:
        pass

    @abstractmethod
    def andar(self, dado: any) -> None:
        pass

    @abstractmethod
    def navegar(self, dado: any) -> None:
        pass


# Modulos de baixo nivel, neles são implementados os metodos especificos de cada veículo
class Aviao(TiposVeiculos):
    def voar(self, dado: any) -> None:
        print(f"{dado} está voando")

    def andar(self, dado: any) -> None:
        pass

    def navegar(self, dado: any) -> None:
        pass


class Carro(TiposVeiculos):
    def andar(self, dado: any) -> None:
        print(f"{dado} está andando")

    def voar(self, dado: any) -> None:
        pass

    def navegar(self, dado: any) -> None:
        pass


class Barco(TiposVeiculos):
    def navegar(self, dado: any) -> None:
        print(f"{dado} está navegando")

    def voar(self, dado: any) -> None:
        pass

    def andar(self, dado: any) -> None:
        pass


# Modulo de alto nivel, nesse caso ele depende das implementações da interface (TiposVeiculos)
# Quando for implementado mais veiculos, não irá ter problema
class Veiculo:
    def __init__(self, tipo_veiculo: Type[TiposVeiculos]) -> None:
        self.tipo_veiculo = tipo_veiculo

    def voar(self, dado: any) -> None:
        self.tipo_veiculo.voar(dado)

    def andar(self, dado: any) -> None:
        self.tipo_veiculo.andar(dado)

    def navegar(self, dado: any) -> None:
        self.tipo_veiculo.navegar(dado)


# Instanciando os veiculos
veiculo = Veiculo(Aviao())
veiculo.voar('Aviao')

veiculo = Veiculo(Carro())
veiculo.andar('Carro')

veiculo = Veiculo(Barco())
veiculo.navegar('Barco')
