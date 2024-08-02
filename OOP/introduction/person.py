"""
Underweight = <18.5
Normal weight = 18.5–24.9
Overweight = 25–29.9
Obesity = BMI of 30 or greater
"""


class Person:
    def __init__(self, first_name, last_name, gender, age, height, weight):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age
        self.height = height
        self.weight = weight

    def info(self):
        print(f'Name: {self.first_name} {self.last_name}')
        print(f'Gender: {self.gender}')
        print(f'Age: {self.age}')
        print(f'Height: {self.height}')
        print(f'Weight: {self.weight}')

        print('\n')

    def _bmi(self):
        return self.weight / self.height ** 2

    def check(self):
        bmi = self._bmi()
        if bmi <= 18.5:
            print('Underweight')
        elif 18.5 < bmi <= 25:
            print('Normal')
        elif 25 < bmi <= 29.9:
            print('Overweight')
        else:
            print('Obesity')


arsen = Person("Arsen", "Kezhegulov", "male", 22, 1.82, 62)
alinur = Person("Alinur", "Azzamov", "male", 16, 1.60, 50)
bilal = Person("Bilal", "Parhidinov", "male", 15, 1.75, 60)
nurlis = Person("Nurlis", "Samatov", "male", 15, 1.68, 56)
baiel = Person("Baiel", "Ergeshov", "male", 14, 1.65, 50)
aibarchyn = Person("Aibarchyn", "Nurgazieva", "female", 19, 1.69, 55)
jyrgal = Person("Jyrgal", "Jailoobekova", "female", 15, 1.60, 45)

for person in [arsen, alinur, bilal, nurlis, baiel, aibarchyn, jyrgal]:
    person.check()
    person.info()

