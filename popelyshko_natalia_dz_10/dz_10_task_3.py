class Cell:
    cell = 0

    def __init__(self, cell: int):
        self.cell = cell

    def __str__(self):
        return str(f'Количество ячеек - {self.cell}')

    def __sub__(self, other):
        return Cell(abs(self.cell - other.cell))

    def __mul__(self, other):
        return Cell(self.cell * other.cell)

    def __truediv__(self, other):
        return Cell(self.cell // other.cell)

    def __add__(self, other):
        return Cell(abs(self.cell + other.cell))

    def make_order(self, count):
        x = self.cell
        while x > 0:
            for k in range(1, count + 1):
                print('*', end='')
                x -= 1
                if x <= 0:
                    break
            print('\n', end='')


a = Cell(10)
b = Cell(20)

print(a + b)
print(a - b)
print(a * b)
print(a / b)

print("==========")
a.make_order(5)
print("==========")
b.make_order(10)
