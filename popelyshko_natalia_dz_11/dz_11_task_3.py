class IntTypeError(Exception):

    @staticmethod
    def int_or_str(value: str):
        if value.isdigit():
            return value
        else:
            raise IntTypeError('Не число')


result_list = []
print(f'--------- Для завершения программы введите "stop". ----------')

while True:
    try:
        user_input = input('Введите число:')
        if user_input == 'stop':
            print('Результат: ', end='')
            print(*result_list)
            break
        else:
            IntTypeError.int_or_str(user_input)
            result_list.append(user_input)
    except IntTypeError as err:
        print(err)