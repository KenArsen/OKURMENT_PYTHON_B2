people = {
    "Arsen": "22",
    "Asan": "25",
}

people["Timur"] = 20
people["Bilal"] = 14
print(people)

name, age = [i for i in input().split()]
people[name] = age
print(people)

del people['Asan']
print(people)

