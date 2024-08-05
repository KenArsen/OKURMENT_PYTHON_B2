class User:
    def __init__(self, name, age, gender):
        self.name = name
        self.__age = age
        self.__gender = gender

    # getter
    # setter

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age < 0:
            print("Jashynyzdy tuura jazynyz!")
        else:
            self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age < 0:
            print("Jashynyzdy tuura jazynyz!")
        else:
            self.__age = age

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        if gender not in ['male', 'female']:
            print("Jynysynyzdy tuura jazynyz(male, female)!")
        else:
            self.__gender = gender


user_1 = User('Asan', 24, 'Male')
print(user_1.name)
print(user_1.get_age())
print(user_1.get_gender())

user_1.set_age(age=28)
user_1.set_gender('female')

print(user_1.get_age())
print(user_1.get_gender())

user_1.set_age(age=-22)
user_1.set_gender('mile')

print(user_1.get_age())
print(user_1.get_gender())

print(user_1.age)
user_1.age = -30
print(user_1.age)

