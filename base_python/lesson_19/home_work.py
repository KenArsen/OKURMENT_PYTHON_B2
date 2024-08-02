# 1 - тапшырма
"""
cities.txt деген бир файлга коносльдон киргизилген шаарлардын аттарын сакташ керек.
Консольдон биз шаар аттарын через пробел менен ажыратып киргизебиз
"""

try:
    cities = [city + "\n" for city in input().split()]
    with open("lesson_19/cities.txt", 'w', encoding="utf-8") as file:
        file.writelines(cities)
except FileNotFoundError:
    print("Mynday file jok!")
finally:
    print("Finished")


# 2 - тапшырма
"""
Ошол жазылган шаар аттарын, файлдын ичинен окуп, 
ар бир шаар атын ознучо бир сапка чыгарыныздар
"""

try:
    with open("lesson_19/cities.txt", 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')
except FileNotFoundError:
    print("Mynday file jok!")
finally:
    print("Finished")