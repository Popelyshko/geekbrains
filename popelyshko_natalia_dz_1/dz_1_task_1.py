

duration = int(input('Введите продолжительность периода: '))
print(duration)

duration = int(input('Введите продолжительность периода: '))
minute = duration // 60
second = duration % 60
print(minute, second)

duration = int(input('Введите продолжительность периода: '))
hour = duration // 3600
minute = (duration % 3600) // 60
second = duration - (hour * 3600 + minute * 60)
print(hour, minute, second)

duration = int(input('Введите продолжительность периода: '))
day = duration // 86400
hour = duration % 86400 // 3600
minute = (duration % 3600) // 60
second = duration - (day * 86400 + hour * 3600 + minute * 60)
print(day, hour, minute, second)




















