N = 100
WIDTH = 150
HIGHT = 200

def fun(lst):
    rec = "Okurmen"
    global WIDTH
    WIDTH = 250
    for i in lst:
        print(i)
    print(rec)
    print(WIDTH)

# fun([1,2,3])
# print(WIDTH)


def fun_1(n):
    print(n)
    def fun_2(m):
        print(m)
        nonlocal n
        n = "Arsen"
        print(n)
    fun_2("Nesra")
    print(n)

fun_1("Okurmen")

name = "Arsen"
def change_name():
    global name
    name = "Nesra"

print(name)
change_name()
print(name)
