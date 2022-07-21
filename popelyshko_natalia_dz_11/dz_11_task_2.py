class ZeroException(Exception):
    def __str__(self):
        return "Ошибка деления на ноль"


a: int = 10
b: int = 1

try:
    if b == 0:
        raise ZeroException()
    else:
        print(f'Результат деления a={a} на b={b}: {a / b}')
except ZeroException as err:
    print(err)