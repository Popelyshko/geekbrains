# получим объект файла
file1 = open("./data/nginx.log", "r")
result_list = []

while True:
    # считываем строку
    line = file1.readline()
    # прерываем цикл, если строка пустая
    if not line:
        break
    split_str = line.split(" ")
    # получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>)
    result_list.append((split_str[0], split_str[5], split_str[6]))
# закрываем файл
file1.close
# выводим кортежи построчно
for line in result_list:
    print(line)
