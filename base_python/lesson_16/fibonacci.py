def fibo(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    
    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append(fib[-1] + fib[-2])
    
    return fib[n-1]

number = int(input())
res = fibo(n=number)
print(res)


