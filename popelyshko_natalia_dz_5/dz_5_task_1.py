def generating(odd_nums):
    for i in range(1, odd_nums + 1, 2):
        yield i

for i in generating(15):
    print(i)

print(generating(15))