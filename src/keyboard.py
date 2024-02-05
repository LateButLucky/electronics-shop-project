from src.item import Item


class SwapLanguage:
    def __init__(self):
        self.__language = 'EN'

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        if self.__language == "EN":
            self.__language = "RU"
        else:
            self.__language = "EN"


class Keyboard(Item, SwapLanguage):
    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
        SwapLanguage.__init__(self)

    def __repr__(self):
        return f"Keyboard({self.name}, {self.price}, {self.quantity}, {self.__language})"
