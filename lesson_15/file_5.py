# def get_all_sum(*args): # упаковка
#     sum_all = 0
#     print(args)
#     for i in args:
#         sum_all += i
#     return sum_all

# res = get_all_sum(1,2,3,4,5,5)
# print(res)


# def info(**kwargs):
#     print(kwargs)

# info(a=2, b=1, c=3, d=6, e=5)


# def fun(*args, **kwargs):
#     print(args, kwargs)

# fun(1,2,3,4,5)
# fun(name="Arsen", age=22, gender="male")
# fun(1, 2, 3, name="Timur", age=19, gender="male")



# (1,2,3,a='one', b="two")
# 1 2 3
# a one
# b two

def fun_1(*args, **kwargs):
    for i in args:
        print(i, end=" ")
    print()
    for key, value in kwargs.items():
        print(key, value)

fun_1(2,3,4,5,city="London", number=12)
