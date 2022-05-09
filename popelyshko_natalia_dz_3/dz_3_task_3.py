def thesaurus(*names: str) -> dict:
    result: dict = {}

    for name in names:
        first_letter = name[0]
        if result.get(first_letter, False):
            result[first_letter].append(name)
        else:
            result[first_letter] = [name]

    return result

print(thesaurus('Иван', 'Мария', 'Петр', 'Илья', 'Моника'))
