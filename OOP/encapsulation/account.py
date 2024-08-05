class Account:
    def __init__(self, email, password):
        self.email = email
        self.__password = password


"""
Аккаунт деген класс, жана анын эки атрибуту болсун(email, password).
password приватный атрибут болсун жана ага геттер менен сеттер жазыныздар!
password - узундугу 8 ден кичине болбош керек!

Бул тапшырманы буткондор учун:
кошумча дагы эки атрибут кошунуздар(first_name, last_name)
анан password - first_name, last_name барабар болбош керек!
"""

