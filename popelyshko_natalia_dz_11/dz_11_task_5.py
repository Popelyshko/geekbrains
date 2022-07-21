class StoreError(Exception):
    pass


class Stock:
    def __init__(self):
        self.stock = {}

    def add(self, equipment, department):
        self.stock.setdefault(department, [])
        self.stock[department].append(equipment)

    def remove(self, equipment, department):
        try:
            self.stock[department].remove(equipment)
        except:
            raise StoreError(f'На складе департамента {department} нет {equipment}')

    def move(self, entity, department_from, department_to):
        self.remove(entity, department_from)
        self.add(entity, department_to)


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
stock.add(scanner, 'Дирекция')
print(stock.stock)
stock.move(scanner, 'Дирекция', 'IT')
print(stock.stock)
