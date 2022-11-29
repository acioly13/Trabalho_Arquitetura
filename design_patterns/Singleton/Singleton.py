# Design Pattern: Singleton

# A minha classe que implementa os metodos
class MyClass:
    def __init__(self, value):
        self.value = value

    def get_value(self):
        print(self.value)

    def set_value(self, new_value):
        self.value = new_value


# Implementando o Singleton de forma simples para não ter 2 espaços de memoria sendo usados
value = MyClass(0)


# Testando o Singleton pode-se obeservar que o espaço de memoria é o mesmo para os 2 elementos
print(f'Espaço de memoria Inicial: {value}')
element1 = value
print('Valor Inicial: ', end='')
element1.get_value()

element1.set_value(1)
print(f'\nEspaço de memoria elemento 1 depois de receber o novo valor: {element1}')
print('Novo Valor: ', end='')
element1.get_value()


elemento2 = value
print(f'\nEspaço de memoria elemento 2: {elemento2}')
print('Valor elemento 2: ', end='')
elemento2.get_value()





