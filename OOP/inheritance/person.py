from OOP.inheritance.begin import Dog


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f'Name: {self.name}\nAge: {self.age}')


class User(Person, Dog):
    def __init__(self, name, age, dog_breed, dog_age, dog_name):
        Person.__init__(self, name, age)
        Dog.__init__(self, dog_breed, dog_age, dog_name)

    def get_person_info(self):
        Person.info(self)

    def get_dog_info(self):
        Dog.info(self)


user = User('John', 20, 'Dog', 2, 'Bob')
user.get_person_info()
user.get_dog_info()
