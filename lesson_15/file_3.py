# return

def get_sum(a, b):
    print(a + b)
    return a + b

s = get_sum(5, 6) # 11
print(s) # 11

def get_area(width, height): # width = 5, height =6
    return width * height # 30

area = get_area(5, 6) # 30
print(area)


def get_sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

res = get_sum([100, 200, 300])
print(res)


def get_info(name, age):
    if age < 12:
        return f"{name}, kids"
    if age >= 12 and age <=18:
        return f"{name}, adult"
    if age > 18:
        return f"{name}, man"

name = input("Name: ")
age = int(input("Age: "))
print(get_info(name, age))