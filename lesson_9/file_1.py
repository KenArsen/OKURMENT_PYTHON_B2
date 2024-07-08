n = int(input("n: "))
m = int(input("m: "))

if n > m:
    k = n
else:
    k = m
print("Simple if", k)

# k = <значение> if <условия> else <значение>

k = n if n > m else m
print("Ternarnyi if", k)

# 3425323 -> san
# aaskfhlf -> tamga
print("san" if input("text: ").isdigit() else "tamga")


