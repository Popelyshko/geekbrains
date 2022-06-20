class Worker:
    name = None
    surname = None
    position = None
    _income = {"profit": 1, "bonus": 2}

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income

class Position(Worker):
    def __init__(self, name, surname, position, income):
        super().__init__(name, surname, position, income)

    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_full_profit(self):
        return self._income["profit"] + self._income["bonus"]


boss = Position('Name', 'Surname', 'boss', {'profit': 1, 'bonus': 2})
print(boss.get_full_name(), boss.get_full_profit())