odd_nums = []
for i in range(1, 300 + 1, 2):
    odd_nums.append(i)

my_gen = (nums for odd_nums in range(1, 300 + 1))
print(odd_nums)