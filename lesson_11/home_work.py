# 1 - тапшырма
"""
Программага шаарлардын аттары боштук(пробел) менен бөлүнүп берилген сап киргизилет. 
Берилген шаарлардын ичинен узундугу беш символдон чон болгон шаарлардын 
аттарын камтыган тизмени(список) түзүү керек. 
Алынган тизмедеги элементтерди бир сапка боштук менен бөлүп чыгарыңыз
Генерациянын жардамы менен чыгарынзыдар

Мисалы:
Bishkek Naryn Talas Osh Chui Jala-Abad

Жоопко:
Bishkek Naryn Talas Jala-Abad
"""

citites = [city for city in input().split()]
for city in citites:
    if len(city) >= 5:
        print(city, end=' ')
print()


# 2 - тапшырма
"""
Программага сандар боштук(пробел) менен бөлүнүп берилет. 
Берилген сандардын ичинен эгер сан 0 дон кичине болсо, "терс",
болбосо "он" деген жазуу турундо башка бир списокко сакталыш керек. 
Генерациянын жардамы менен чыгарынзыдар

Мисалы:
1 -3 -2 4 2 5

Жоопко:
['он', 'терс', 'терс', 'он', 'он', 'он']
"""

numbers = [int(i) for i in input().split()]
result = []
for number in numbers:
    if number > 0:
        result.append("+")
    else:
        result.append("-")
print(result)

# 3 - тапшырма
"""
Программага бир сан киргизилет.
Сиздер ошол сандын жадыбалын(таблица умножение) чыгарышыздар керек.

Мисалы:
4

Жоопко:
4 * 1 == 4
4 * 2 == 8
4 * 3 == 12
4 * 4 == 16
4 * 5 == 20
4 * 6 == 24
4 * 7 == 28
4 * 8 == 32
4 * 9 == 36
4 * 10 == 40
"""

n = int(input("n: "))
for i in range(1, 11):
    print(f"{n} * {i} = {n * i}")
