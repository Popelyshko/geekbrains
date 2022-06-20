tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Едена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']


def gen_peopl():
    i = 0
    c = 0
    while i < len(klasses):
        if i >= len(tutors):
            yield (None, klasses[i])
            i += 1
            c += 1
            break
        else:
            yield (tutors[c], klasses[i])
            i += 1
            c += 1


for gen in gen_peopl():
    print(gen)
