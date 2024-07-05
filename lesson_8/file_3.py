# if <условия>:
#     оператор 1
#     оператор 2
#     оператор 2
#     .....
#     оператор n
# else:
#     оператор 1
#     оператор 2
#     оператор 2
#     .....
#     оператор n

x = 4

if x < 0:
    x = -x
    print(x)
else:
    print("print")
    
print(x)

# bool (True, False)
# str ("")
# int (-n, ..., -2, -1, 0, 1, 2, 3, ..., n)
# float -> (4.5, 3.55, 12.4)


print(type(-2))
print(type(-3.55))
print(type("89725"))
print(type(True))


# n = input('Введите одно число: ')

# if n.isdigit():
#     n = int(n)
# else:
#     print("San jazynyz")

# print(type(n))

# 2
# 4

# num_1 = int(input("Введите первое число: "))
# num_2 = int(input("Введите второе число: "))

# if num_1 > num_2:
#     print(num_1)
# else:
#     print(num_2)


# text_1 = input("Введите первый текст: ")
# text_2 = input("Введите второй текст: ")

# if text_1 == text_2:
#     print("Barabar")
# else:
#     print("Barabar emes")

# green (3)
# red (2)
# 10
# 1 g 1
# 2 g 2
# 3 g 3
# 4 r 4
# 5 r 0
# 6 g 1
# 7 g 2
# 8 g 3
# 9 r 4
# 10 r 0
# 11 g 1
# 12 g 2
# 13 g 3
# 14 r 4
# 15 r 0
# 16 g 1
# 17 g 2
# 18 g 3
# 19 g 4
# 20 r 0

# 70 % 5 -> 0,1,2,3,4

n = int(input("Введите минуту: "))
m = n % 5
# if m >= 1 and m <= 3:
if 1 <= m <= 3:
    print("green")
else:
    print("red")





