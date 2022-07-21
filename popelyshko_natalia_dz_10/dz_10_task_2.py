from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @abstractmethod
    def fabric_consumption(self):
        pass


class Coat(Clothes):

    @property
    def fabric_consumption(self):
        return self.param / 6.5 + 0.5


class Suit(Clothes):

    @property
    def fabric_consumption(self):
        return 2 * self.param + 0.3


coat = Coat(42)
suit = Suit(1.60)
print(coat.fabric_consumption)
print(suit.fabric_consumption)
