# Запись данных
import sys
from typing import List


def write_base():
    input_data: int = int(sys.argv[1])
    with open('./data/task_6.txt', 'a') as file:
        file.write(str(input_data) + "\n")


def print_base():
    base = open("./data/task_6.txt", "r").readlines()
    if len(sys.argv) == 1:
        print_line(base)
    if len(sys.argv) == 2:
        print_line(base[int(sys.argv[1]) - 1:])
    if len(sys.argv) == 3:
        print_line(base[int(sys.argv[1]) - 1:int(sys.argv[2])])


def print_line(base: List[str]):
    for line in base:
        print(line.replace("\n", ""))


# print_base()
# write_base()
