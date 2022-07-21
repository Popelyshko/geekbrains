class StoreError(Exception):
    pass


class ValidateError(Exception):
    pass


class Stock:
    def __init__(self):
        self.stock = {}

    def valid_amount(self, n):
        if n.isdigit():
            pass
        else:
            raise ValidateError("Ошибка валидации")

    def add(self, amount, equipment, department):
        self.valid_amount(amount)
        self.stock.setdefault(department, [])
        self.stock[department].append(equipment)

    def remove(self, amount, equipment, department):
        self.valid_amount(amount)
        try:
            self.stock[department].remove(equipment)
        except:
            raise StoreError(f'На складе департамента {department} нет {equipment}')

    def move(self, entity, department_from, department_to):
        self.remove("1", entity, department_from)
        self.add("1", entity, department_to)


class Equipment:
    def __init__(self, name):
        self.name = name


class Printer(Equipment):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size


class Scanner(Equipment):
    def __init__(self, name, is_color):
        super().__init__(name)
        self.is_color = is_color


class Xerox(Equipment):
    def __init__(self, name, is_multipage):
        super().__init__(name)
        self.is_multipage = is_multipage


stock = Stock()
scanner = Scanner('Samsung', True)
stock.add("2", scanner, 'Дирекция')
print(stock.stock)
stock.move(scanner, 'Дирекция', 'IT')
print(stock.stock)
