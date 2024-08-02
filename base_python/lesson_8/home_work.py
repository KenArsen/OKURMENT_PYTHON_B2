# 1 - тапшырма
numbers = [[2, 4, 6, 8], [1, 3, 5, 7, 9]]
"""
numbers списоктун ичинен 0 - индекстеги жана 1 - индекстеги 
списоктун элементтеринин суммасын чыгарыныздар! 
"""
print(numbers[0][0] + numbers[0][1] + numbers[0][2] + numbers[0][3])
print(numbers[1][0] + numbers[1][1] + numbers[1][2] + numbers[1][3] + numbers[1][4])


# 2 - тапшырма
countries = [["Kyrgyzstan", "Kazakstan"], ["Paris", "Italiya"], ["USA", "Canada"]]
"""
жоопко
Kyrgyzstan
Italiya
Canada

ушинтип чыгарыныздар!
"""

print(countries[0][0])
print(countries[1][1])
print(countries[2][1])

# 3 - тапшырма
"""
Консольдон бир текст киргизебиз(input() менен).
Эгер жазылган текст Okurmen деген созго барабар болсо 'YES' болбосо 'NO' деп чыгарыныздар!
"""

name = input("Введите один текст: ")
if name == "Okurmen":
    print("YES")
else:
    print("NO")