"""
Консольдон атын жана фамилиябызды киргизебиз.
Анан функция жазыныздар, ал бизге мындай 
маалымат чыгарсын:
"Урматтуу <аты> <фамилиясы>. Сиз бул программаны туура аткардыныз"
"""

def get_msg(a, b):
    print(f'Урматтуу {a} {b}. Сиз бул программаны туура аткардыныз')

name = input("Enter your name: ")
surname = input("Enter your surname: ")
get_msg(name, surname)




"""
Фунция жазыныздар, ал фукция бизге торт бурчтуктун аянтын эсептеп берсин.
Фунция эки параметр алат(width жана height) узуну жана туурасы.
Эки санды коносольдон киргизебиз(инпут менен)
"""

def get_area(width, height):
    print(f"Area = {width * height}")


n = int(input("Width: "))
m = int(input("Height: "))
get_area(n, m)


