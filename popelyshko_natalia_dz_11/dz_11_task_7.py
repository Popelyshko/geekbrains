class Complex():

    def __init__(self, int1, int2):
        self.int1 = int1
        self.int2 = int2

    def __add__(self, other):
        return (self.int1 + other.int1) + self.int2 + other.int2

    def __mul__(self, other):
        return (self.int1 * other.int1 - self.int2 * other.int2) + (self.int1 * other.int2 + self.int2 * other.int1)


a = Complex(1, 1)
b = Complex(2, 2)

print(a + b)
print(a * b)