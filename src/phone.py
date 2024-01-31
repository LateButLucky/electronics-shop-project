from src.item import Item


class Phone(Item):

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value):
        if int(value) >= 0:
            self.__number_of_sim = int(value)
        else:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')

    def __repr__(self):
        return f"Phone('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __str__(self):
        return self.name

    def __add__(self, other):
        if not isinstance(other, Item):
            print('Класс не является дочерним классом Item')

        return self.quantity + other.quantity

    def __radd__(self, other):
        if not isinstance(other, Item):
            print('Класс не является дочерним классом Item')

        return other.quantity + self.quantity
