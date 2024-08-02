# 1 2 3 4 6 7 8 4 5

names_text = input("Введите имя: ")

names = [f'{name}: {len(name)}' for name in names_text.split()]
print(names)

["Arsen: 5", "Ali: 3", "Timur: 5"]


