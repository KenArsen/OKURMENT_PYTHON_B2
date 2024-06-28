# str
name_1 = "Panda_1"
name_2 = 'Panda_2'
name_3 = """
My name is Okurmen,
I live in Bishkek
"""
number = '12'

print(name_1 + " " + name_2 + " " + name_1)
# Panda_1 Panda_2 Panda_1
print(name_1 + number)

# len() бул текстин узундугун эсептейт
# тексттин ичинде канча символ бар экенин эсептеп берет
person = " Okurmen"
print(len(person))

# in
country = "Kyrgyzstan"
word = "kyrgyz"
a = word in country
print(a)

# ==, !=, >, <, >=, <=
city_1 = "Bishkek"
city_2 = "Talas"
city_3 = "BishkeKA"
a = city_1 == city_3
b = city_1 < city_3
print(a)
print(b)
print(ord("+"))


