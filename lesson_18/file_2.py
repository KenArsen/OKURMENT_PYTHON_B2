from datetime import datetime


def get_time(func):
    def wrapper(n):
        start_time = datetime.now()
        func(n)
        end_time = datetime.now()
        return end_time - start_time
    return wrapper

def fibo(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibo(n - 1) + fibo(n - 2)

fibo = get_time(fibo)
time = fibo(35)
print(time)
