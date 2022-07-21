class Stock:
    def __init__(self):
        self.stock = []


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

