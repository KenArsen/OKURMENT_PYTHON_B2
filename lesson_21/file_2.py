"""
annotations >= Python 3.5
Для удобства восприятия стороннего кода.
Для удобства редактирования кода, когда IDE «подсказывает» атрибуты указанного типа переменных.
Для отслеживания некоторых явных ошибок на уровне несоответствия типов.
"""

"""
Expected type 'int', got 'str' instead
Ожидаемый тип «int», вместо этого получен «str»
"""

"""
int, float, str, bool
"""

"""
version >= Python 3.9 
list, tuple, dict, set
list[int], list[str], list[float], list[bool], list[None]
tuple[int, str, float, bool, ....], tuple[str], tuple[float], tuple[bool]
set[int], set[str], set[float], set[bool]
dict[str, int], dict[str, int], dict[str, float], dict[str, bool]

version < Python 3.9
from typing import List, Tuple, Dict, Set

начиная с версии Python 3.10, эту же нотацию можно определить и так
list[int | float]

"""

number:int = 23

def get_div(a:int, b:int):
    return a / b

def get_sum_all(numbers:list[int|float]):
    return sum(numbers)

def fun(numbers:tuple[int, float, str, bool, int]):
    print(numbers)

def fun_1(data:dict[int, str]):
    pass

fun(numbers=(True, 1, 2.3, "Okurmen", True))