"""
https://docs.python.org/3/library/index.html
import random
random.random() -> Она при каждом вызове выдает случайное значение в диапазоне [0.0; 1.0).

random.uniform(1, 5) -> Другая похожая функция uniform(a, b) также генерирует случайные значения,
                        но в диапазоне от a до b:

random.randint(-3, 7) -> Если нам нужно моделировать целочисленные случайные значения,
                        то можно использовать или функцию:
                        [-3; 7]

lst = [4, 5, 0, -1, 10, 76, 3]
random.choice(lst) -> random при работе с последовательностями
                        выбрать один элемент случайным образом

random.shuffle(lst) -> Следующая функция shuffle() перемешивает элементы списка случайным образом:
                        Причем, меняет сам список, поэтому работает только с изменяемыми коллекциями.

random.sample(lst, 3) -> sample() возвращает новый список с указанным числом неповторяющихся элементов,
                            выбранных случайным образом из списка:
                            Разумеется, максимальное число элементов не может превышать число элементов в списке lst.

"""

import random
print(random.random()) # [0.0, 1.0)
print(random.uniform(2.4, 2.6))
print(random.randint(-5, 0))
lst = [4, 5, 0, -1, 10, 76, 3]
print(random.choice(lst))
random.shuffle(lst)
print(lst)
print(random.sample(lst, 3))


names = ["Arsen", "Alinur", "Aibarchyn", "Baiel", "Bilal", "Saule", "Jyrgal", "Nurlis"]
ramdom_name = random.choice(names)
print(ramdom_name)
name = input("Name: ")
print(ramdom_name == name)

