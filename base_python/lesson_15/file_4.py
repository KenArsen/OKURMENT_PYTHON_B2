def fun_1(a, b, c): # фактические параметры
    pass

def fun_2(name="Okurmen", age=18): # формальные параметры
    pass


fun_1(1, 2, 3) # порядковые аргуметы
fun_1(b=1, c=2, a=3) # именованные аргуметы
fun_2(name="Arsen", age=22) # именованные аргуметы


def get_sum(a, b, c, is_verbose=True):
    if is_verbose:
        print(f'a = {a}, b = {b}, c = {c}')
    return a + b + c

res = get_sum(2, 4, 5, is_verbose=False)
print(res)
