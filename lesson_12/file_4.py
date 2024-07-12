# 1 - task
data = {
    "Lenevo": 2024,
    "Dell": 2020,
    "Macbook": 2022,
    "HP": 2019,
    "Acer": 2016,
    "Xiomi": 2024
}

model = input("Model: ")
year = int(input("Yeer: "))
data[model] = year
print(data)

# 2 - task
people = dict()
name = input("Name: ")
age = int(input("Age: "))

if age < 12:
    people[name] = "kid"
elif 12 <= age < 18:
    people[name] = "adult"
else:
    people[name] = "man"

print(people)

# 3 - task
data = {
    "Arsen": 22,
    "Timur": 19,
    "Aibarchyn": 19,
    "Jurgal": 15,
    "Malika": 15,
    "Bilal": 15,
    "Daniel": 15,
    "Baiel": 15,
    "Nurlis": 15,
}

for name, age in data.items():
    print(name, age)
    if age < 12:
        data[name] = 'kid'
    elif 12 <= age < 18:
        data[name] = 'adult'
    else:
        data[name] = 'man'

print("\n\n")
for key, value in data.items():
    print(key, value)

    
