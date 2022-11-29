# Design Pattern: Facade
from Delete import Delete
from Insert import Insert
from Select import Select


# Fachada para os metodos complexos
class Facade:
    def __init__(self):
        self.select = Select()
        self.insert = Insert()
        self.delete = Delete()

    def select_one(self):
        return self.select.select_single_element()

    def select_many(self):
        return self.select.select_many_elements()

    def insert_one(self):
        return self.insert.insert_single_element()

    def insert_many(self):
        return self.insert.insert_many_elements()

    def delete_one(self):
        return self.delete.delete_single_element()


# Teste da fachada
fachada = Facade()
fachada.select_one()
