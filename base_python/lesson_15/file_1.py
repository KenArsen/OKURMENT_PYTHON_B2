"""
def <name>(parametrs, par...):
    operator 1
"""
# n
# 1..10 - > 1 2 3 4 5 6 7 8 9 10
# 1 3 5 7 9
# 2 4 6 8 10
# 

def get_digits(number): # 5
    jup_numbers = []
    tak_numbers = []
    for i in range(1, number + 1): # 1,2,3,4,5
        if i % 2 == 0:
            jup_numbers.append(i)
        else:
            tak_numbers.append(i)
    print(jup_numbers)
    print(tak_numbers)


def factorial(n): # n -> paramentr
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)

def sum_a_b(a, b):
    print("a = ", a)
    print("b = ", b)
    print("sum = ", a + b)


# sum_a_b(4, 5)
# factorial(10) # 10 -> argument
# factorial(15)
get_digits(20)

def get_max(n, m):
    sum_a_b(n, m)
    if n > m:
        print(n)
    elif m > n:
        print(m)
    else:
        print("Barabar")


get_max(3, 5)



