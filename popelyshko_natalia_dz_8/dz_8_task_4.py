import functools


def val_checker(validator_func):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(arg, **kwargs):
            if not validator_func(arg):
                raise ValueError("Ошибка валидации параметра")
            return func(arg, **kwargs)

        return wrapper

    return decorator


@val_checker(lambda x: x > 0)
def calc_cube(x: int):
    return x * 3


print(calc_cube(5))
