# lambda параметры: <условие>

fun = lambda x, y: x + y
upper = lambda text: text.upper()
num = lambda n: "on" if n > 0 else "ters"
print(num(1))
print(num(-1))

print(fun(5, 6))
print(upper("Arsen"))

cities = ["Bishek", "Talas", "Naryn", lambda x: x.isalpha()]
print(cities)
print(cities[3]("Okurmen"))
print(cities[3]("1234"))