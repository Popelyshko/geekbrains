import random
from random import randint


def get_jokes(quantity: int):
    """
    Функция формирует случайные шутки из трех списков слов.
    """
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    result = []
    for i in range(0, quantity):
        result.append(
            nouns[randint(0, len(nouns) - 1)] + ' ' + random.choice(adverbs) + ' ' + random.choice(adjectives))
    return result

print(get_jokes(4))
