# 1 - тапшырма
"""
Программага пробел менен ажыратылган сандарды киргизебиз.
Берилген сандардын ичинен терс сандарды он санга айландырып чыгарыныздар
map функциясынын жардамы менен аткарыныздар

Мисалы:
-5 6 8 11 -10 0

Жооп:
5 6 8 11 10 0
"""

numbers = list(map(int, input().split()))
result = map(lambda x: x if x > 0 else -x, numbers)
result_abs = list(map(lambda x: abs(x), numbers))
print(result_abs)
print(list(result))


# 2 - тапшырма
"""
Программага томонкудой форматта сап(строка) киргизилет:
key_1=value_1 key_2=value_2 .... key_n=value_n

буларды кайра
(('key_1', 'value_1'), ('key_1', 'value_1'), ..., ('key_n', 'value_n'))
деп кортеж тибинде чыгарыныздар.
map функциясынын жардамы менен аткарыныздар
"""

def parse_data(data):
    return tuple(map(lambda x: tuple(x.split("=")), data))

dic = list(map(str, input().split()))
print(parse_data(data=dic))


# 3 - тапшырма
"""
Программага боштук менен бөлүнгөн бүтүн сандар киргизилет. 
Бул сандарды окуп, алардын ичинен эки орундуу сандарды гана калтыруу керек. 
Программаны filter функциясын колдонуп ишке ашыруу керек. 
Натыйжаны бир сапка боштук менен бөлүп экранга чыгарыңыз.

Мисалы:
8 11 0 -23 140 1

Жоопко:
11 -23
"""

def get_number(n):
    return 10 <= n <= 99 or -99 <= n <= -10

numbers = list(map(int, input().split()))
res = filter(get_number, numbers)
print(list(res))
