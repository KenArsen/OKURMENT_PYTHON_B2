class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __add__(self, other):
        return Person(self.name, self.age + other.age, self.gender)

    def __truediv__(self, other):
        if isinstance(other, Person):
            return Person(self.name, self.age / other.age, self.gender)
        else:
            return Person(self.name, self.age / other, self.gender)

    def info(self):
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Gender: {}".format(self.gender))


asan = Person("Asan", 24, "Male")
uson = Person("Uson", 24, "Male")
argen = Person("Argen", 22, "Male")
arnas = Person("Arnas", 22, "Male")

res_add = uson + asan + argen + arnas
res_div_1 = uson / asan
res_div = uson / 10
# uson + asan = ob + argen = ob + arnas = ob
res_add.info()
res_div.info()
res_div_1.info()
