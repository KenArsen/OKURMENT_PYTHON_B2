class Account:
    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.__password = password

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        if password == self.first_name:
            print("Password is same as first name")
        elif password == self.last_name:
            print("Password is same as last name")
        elif len(password) < 8:
            print("Password must be at least 8 characters")
        else:
            self.__password = password


account = Account("Arsen", "Kenzhegulov", "example@gmail.com", "12345")
print(account.email)
print(account.password)

account.password = "123456789"
print(account.password)

account.password = "Arsen"
print(account.password)

account.password = "Kenzhegulovich"
print(account.password)


"""
Аккаунт деген класс, жана анын эки атрибуту болсун(email, password).
password приватный атрибут болсун жана ага геттер менен сеттер жазыныздар!
password - узундугу 8 ден кичине болбош керек!

Бул тапшырманы буткондор учун:
кошумча дагы эки атрибут кошунуздар(first_name, last_name)
анан password - first_name, last_name барабар болбош керек!
"""
