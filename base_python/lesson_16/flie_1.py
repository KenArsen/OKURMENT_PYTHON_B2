def fibbonaci(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibbonaci(n - 1) + fibbonaci(n - 2)


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


res = factorial(5)
print(res)