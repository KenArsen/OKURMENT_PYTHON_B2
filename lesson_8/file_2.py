# ==
# if - если - егер
# else - антпесе, болбосо
# elif - else if

num_1 = 201
num_2 = 200
num_3 = 150

if num_1 > num_2 and num_1 < num_3: # False
    print("if ishtedi")
    print(num_1 - num_2)
else:
    print("else ishtedi")
    print(num_2 - num_1)

# True and False

a = 13
b = 3
c = 2

if a > b and a > c:
    print(a) 
elif b > a and b > c:
    print(b)
else:
    print(c)

# Okurmen -> 7
# YES
# Oku -> 3
# NO

text = input("Введите текст: ")
if len(text) > 5:
    print("YES")
else:
    print("NO")
