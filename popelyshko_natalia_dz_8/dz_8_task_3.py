def type_logger(func):
    def wrapper_type(*args):
        for item in args:
            print(type(item))
        return func(*args)
    return wrapper_type


@type_logger
def calc_cube(x: int):
    return x ** 3


print(calc_cube(5))
