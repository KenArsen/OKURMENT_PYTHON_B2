def get_sum(n):
    total = 0
    for i in n:
        total += int(i)
    return total

numbers = ['234', '456', '99', '11111111']
result = sorted(numbers, key=lambda x: get_sum(x))
print(result)

"""
Тапшырма 1: Тизменин уникалдуу элементтерин сорттоо

Программага бүтүн сандардын тизмеси берилет.
Биринчилерден уникалдуу элементтерди табып
жана сорттоп чыгарыныздар.
"""

numbers = [6,6,6,7,7,2,2,2,4,4,4,5,5]
print(sorted(set(numbers)))



"""
Тапшырма 2: 

Программага бүтүн сандардын тизмеси берилет. 
Бардык элементтердин суммасын эсептеп, 
сумма ар бир элементке бөлүнүп жатканын текшериниздер.
Эгер баарына болунсо True болбосо False чыгарынзыдар!
"""

numbers = [2,4,6]
s = sum(numbers)
res = [True if s % i == 0 else False for i in numbers ]
print(all(res))