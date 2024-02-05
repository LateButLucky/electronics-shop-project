import pytest
from src.keyboard import Keyboard


@pytest.fixture
def keyboard_fixture():
    return Keyboard('Dark Project KD87A', 9600, 5)


def test_default_language_is_en(keyboard_fixture):
    assert keyboard_fixture.language == 'EN'


def test_swap_language_to_ru(keyboard_fixture):
    keyboard_fixture.change_lang()
    assert keyboard_fixture.language == 'RU'


def test_double_swap_language(keyboard_fixture):
    keyboard_fixture.change_lang()
    keyboard_fixture.change_lang()
    assert str(keyboard_fixture.language) == "EN"


def test_error_language(keyboard_fixture):
    with pytest.raises(AttributeError):
        keyboard_fixture.language = 'CH'


def test___str__(keyboard_fixture):
    assert str(keyboard_fixture) == "Dark Project KD87A"
