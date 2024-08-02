"""
Генератор - итератор, элементы которого можно итерировать только один раз

Итератор - объект, который поддерживает функцию next()

Итерируемый объект - объект, который предоставляет возможность обойти
поочередно свои элементы
"""

# map(func, *iterable)
# filter(func, *iterable)
# zip()

def get_jup(numbers):
    for i in numbers:
        if i % 2 == 0:
            yield i


numbers = [1,2,3,4,5]
a = get_jup(numbers=numbers)
print(next(a))
print(next(a))
print(next(a))