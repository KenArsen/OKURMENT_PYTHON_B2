# 1 - тапшырма
"""
get_total деген фунция болсун, анын эки оргументи
numbers(фактический) жана is_sum(формальный, по умолчанию True)
эгерде is_sum труу болсо, анда берилген numbers тин суммасын,
болбосо кобойтундусун тапкан эки фунция жазыныздар
алар get_sum жана get_multiple деген фунциялар болсун.
Буларды замыкание жардамы менен чыгарыныздар!
"""

def get_total(numbers, is_sum=True):
    def get_sum():
        total = 0
        for number in numbers:
            total += number
        return total
    
    def get_multiple():
        total = 1
        for number in numbers:
            total *= number
        return total
    
    print(get_sum)
    print(get_multiple)
    
    if is_sum:
        return get_sum
    return get_multiple

f_1 = get_total([1,2,3,4,5])
f_2 = get_total([1,2,3,4,5], is_sum=False)
print(f_1)
print(f_2())

