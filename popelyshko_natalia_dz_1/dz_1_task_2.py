    #Список из кубов нечетных чисел от 1 до 1000
list_cube = []

for list_odd_namber in range(1, 1001, 2):
    list_cube.append(list_odd_namber ** 3)
print(list_cube)

total_sum = 0

for list_item in list_cube:
    item_sum = sum(map(int, str(list_item)))

    if item_sum % 7 == 0:
        print(f'число: {list_item}')
        print(f'сумма: {item_sum}')
        print(f'делимость: {item_sum % 7}')
        total_sum = total_sum + list_item

print(total_sum)







