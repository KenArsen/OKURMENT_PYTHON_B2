# bool ->  True, False
# >
# <
# ==
# !=
# >=
# <=
a = True
b = 4

# and, or, not
# жана, же, жо
# и, или, не
a = 5
b = 3
print(a > b and b > 1 and a < 3)
# True  True False
# True * True * False
# 1 * 1 * 0 = 0 -> False

c = 34
d = 23
print(c - 10 > d and d + 11 >= c or d == c)
#34-10>23 and 23+11>=34 or 23==34
#true and true or false
#1 * 1 + 0 = -> true

c = 10
d = 12
print(
    d - 10 > c # 12 - 10 > 10 -> False
    or d + 11 >= c  # 12 + 11 >= 10 -> True
    or d == c # 12 == 10 -> False
    or d + c != d + 20 # 12 + 10 != 12 + 20 -> False
    and d * 5 == c + 50 # 12 * 5 == 10 + 50 -> True
)

# False + True + False + False * True = True

x = 6
k = not x % 2 == 0 or x % 3 == 0