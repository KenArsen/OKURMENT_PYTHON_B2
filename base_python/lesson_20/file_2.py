# .sort()
# sorted()

numbers = [19, 28, 37, 46, 55, 64, 73]
sort_numbers = sorted(numbers, key=lambda x: x % 10)
print(sort_numbers)

names = ["Jyrgal", "Saule", "Aibarchyn", "Baiel", "Nurlis", "Bilal", "Arsen"]
print(sorted(names,reverse=True, key=lambda x: len(x)))
print(sorted(names, key=lambda x: x[1]))


numbers = ['99', '11111111111111', '54', '12', '83', '56', '98']
print(sorted(numbers, key=lambda x: int(x[0]) + int(x[-1])))



