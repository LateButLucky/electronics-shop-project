from src.phone import Phone

phone1 = Phone("iPhone 14", 120_000, 5, 2)


def test_get_number_of_sim():
    assert phone1.number_of_sim == 2


def test_repr():
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"


def test_str():
    assert str(phone1) == 'iPhone 14'
