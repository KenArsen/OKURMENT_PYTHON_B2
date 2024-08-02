phones = ["Iphone 14", "Redmi 12", "Samsung A52", "Poco M3"]

# 1 - тапшырма
"""
phones списоктун ичинен Redmi 12 телефонду удалить кылыныздар!
""" 
phones.remove("Redmi 12")
phones.pop(1)

# 2 - тапшырма
"""
phones списоктун ичинен акыркы элементти удалить кылыныздар!
""" 
phones.pop()

# 3 - тапшырма
"""
phones списоктун эн башына 'Iphone 15' деген элементти кошунуздар!
""" 
phones.insert(0, "Iphone 15")

# 4 - тапшырма
"""
phones списогуна дагы башка эки элемент кошунуздар!
""" 
phones.extend(["Poco M2", "Poco M1"])

# 5 - тапшырма
"""
Консольдон биз адамдын атын(name), фамилиясын(surname) жана жашын(age) алалы(input() жардамы менен),
андан кийин аларды чыграрыш керек
'Уважаемый <имя> <фамилия>! Поздравляем Вас с <возраст>-летием!'
же 
'Dear <name> <surname>! Happy <age>nd birthday!'

Мисалы:
Arsen
Kenzhegulov
22

Жоопко:
Уважаемый Arsen Kenzhegulov! Поздравляем Вас с 22-летием!
же
Dear Arsen Kenzhegulov! Happy 22nd birthday!
""" 
name = input("Введите свое имя: ")
surname = input("Введите свая фамилия: ")
age = input("Введите ваш возраст: ")

print(f"Dear {name} {surname}! Happy {age}nd birthday!")