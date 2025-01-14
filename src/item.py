import csv
from pathlib import Path


class InstantiateCSVError(Exception):
    def __init__(self, csvfile):
        self.csvfile = csvfile

    def __str__(self):
        return f'Файл {self.csvfile} поврежден'


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity

        self.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.__name}"

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) <= 10:
            self.__name = value
        else:
            self.__name = value[:10]

    @classmethod
    def instantiate_from_csv(cls, csvfile='../src/items.csv'):
        cls.all.clear()
        csvfile = Path(__file__).parent.joinpath(csvfile)

        try:
            with open(csvfile, 'r', newline='', encoding='windows-1251') as file:
                reader = csv.DictReader(file)
                for emp in reader:
                    cls(emp['name'], float(emp['price']), int(emp['quantity']))
        except KeyError:
            raise InstantiateCSVError("items.csv")
        except FileNotFoundError:
            raise FileNotFoundError(f"Отсутствует файл items.csv")

    @staticmethod
    def string_to_number(valuestr):
        return int(float(valuestr))
