# loop, цикл


# for <озгормо> in range(start, end, step):
    # operator 1
    # operator 1
    # operator 1
    # operator 1
    # print("okurmen")

n = int(input("N: "))
sum_total = 0
s = 1
for i in range(1, n + 1): # [1 2 3 4 5]
    sum_total = sum_total + i # 1 3 6 10 15
    s = s * i
print(sum_total)
print(s)


# n = 5
# m = 10

n = int(input("N: "))
m = int(input("M: "))

s = 0
t = 1
