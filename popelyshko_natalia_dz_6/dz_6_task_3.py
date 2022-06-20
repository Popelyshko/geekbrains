users = open("./data/users.csv", "r").readlines()
hobby = open("./data/hobby.csv", "r").readlines()

if len(users) < len(hobby):
    exit(1)

result = {}

for i in range(len(users)):
    fio = users[i].replace(",", " ").replace("\n", "")

    if i+1 > len(hobby):
        result[fio] = 'None'
    else:
        result[fio] = hobby[i]

f = open("./data/task_3_result.txt", 'w')
f.write(str(result))
f.close()
