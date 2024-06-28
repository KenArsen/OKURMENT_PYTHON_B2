# 1 - тапшырма
x = 10
a = not (x % 2 == 0 or x % 3 == 0)
print(a)
# not(True or False) -> not(True) -> False

# 2 - тапшырма
b = not x % 2 == 0 or x % 3 == 0
print(b)
# False or False -> False


# 3 - тапшырма
c = x % 2 != 0 or x % 3 == 0
print(c)
# False or False -> False

# 4 - тапшырма 
d = x % 2 != 0 and x % 3 != 0
print(d)
# False and False -> False

'''
Жогорудагы тапшырмаларга тушундурмо жазыныздар
Биз сабакта откондой кылып
'''
