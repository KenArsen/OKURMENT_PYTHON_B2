cities = ["Bishkek", "Talas", "Naryn"]
numbers = [2,5,3,1,7,8]
name = "Okurmen"

for city in cities:
    print(city)

for number in numbers:
    print(number)

for i in name:
    print(i)

# enumerate
for index, value in enumerate(name):
    if index > 1:
        print(f'{index} - {value}')