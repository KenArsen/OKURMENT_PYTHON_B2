class Animal:
    def __init__(self, breed, age):
        self.__breed = breed
        self.__age = age

    def info(self):
        print(f'Breed is {self.__breed}\nAge is {self.__age}')


class Dog(Animal):
    def __init__(self, breed, age, name):
        super().__init__(breed, age)
        self.name = name

    def info(self):
        print(f'Name is {self.name}')
        super().info()


# animal_1 = Animal("Ofcherka", 2)
# animal_1.info()
# print('#' * 10)
# dog_1 = Dog('haski', 3, 'Bob')
# dog_1.info()
#
# # Employee
