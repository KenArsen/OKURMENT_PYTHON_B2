# str => ""
# list => [], list()
# name = "Okurmen"
# name[0] = "A"
# print(name)
cities = ["Bishkek", "Astana", "Osh", "Stambul"]
print(cities)
cities[2] = "Talas"
print(cities)
cities[-2] = "Frunze"
print(cities)
print(cities[1:3:2])

# append(element)
cities = ["Bishkek", "Astana", "Osh", "Stambul"]
cities.append(["Moscow", "London"])

# extend()
cities = ["Bishkek", "Astana", "Osh", "Stambul"]
cities.extend(["Madrid", "Paris"])

# insert()
cities = ["Bishkek", "Astana", "Osh", "Stambul"]
cities.insert(0, "Naryn")
cities.insert(2, "Berlin")
cities.insert(5, "Rome")


# pop()
cities = ["Bishkek", "Astana", "Osh", "Stambul"]
d = cities.pop()
print(d)
d = cities.pop()
print(d)
cities.pop(1)
print(cities)

# remove()
cities = ["Bishkek", "Astana", "Osh", "Stambul", "Bishkek"]
cities.remove("Bishkek")
print(cities)

# reverse()
cities = ["Bishkek", "Astana", "Osh", "Stambul"]
cities.reverse()
print(cities)

# clear()
cities = ["Bishkek", "Astana", "Osh", "Stambul"]
cities.clear()
print(cities)

# sort()
numbers = [2,1,6,3,8,4,9,3,4]
numbers.sort()
print(numbers)

