"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
from src.phone import Phone


def test_calculate_total_price():
    item1 = Item("Картошка", 120, 100)
    assert item1.calculate_total_price() == 12000

    item2 = Item("Морковка", 40, 200)
    Item.pay_rate = 0.8
    item2.apply_discount()
    assert item2.calculate_total_price() == 6400

    item3 = Item("Смартфон", 10000, 20)
    item4 = Item("Ноутбук", 20000, 5)
    Item.pay_rate = 0.8
    item3.apply_discount()
    assert item3.price == 8000.0
    assert item4.price == 20000


def test_instantiate_from_csv():
    Item.instantiate_from_csv("items.csv")
    assert len(Item.all) == 5

    item = Item.all[0]
    assert item.name == 'Смартфон'

    item.name = 'Телефон'
    assert item.name == 'Телефон'

    item.name = 'СуперСмартфон'
    assert item.name == 'СуперСмарт'


def test_string_to_number():
    assert Item.string_to_number('10') == 10
    assert Item.string_to_number('10.0') == 10
    assert Item.string_to_number(10.10) == 10


def test_repr():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"


def test_str():
    item1 = Item("Смартфон", 10000, 20)
    assert str(item1) == 'Смартфон'


phone1 = Phone("iPhone 14", 120_000, 5, 2)
item2 = Item("Смартфон", 10000, 20)


def test_add():
    assert item2 + phone1 == 25
    assert phone1 + phone1 == 10


def test_error_number_of_sim():
    assert ("ValueError: Количество физических SIM-карт должно быть целым числом больше нуля." ==
            "ValueError: Количество физических SIM-карт должно быть целым числом больше нуля.")
