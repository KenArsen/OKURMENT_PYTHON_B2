class Cat:
    def __init__(self, name, age, breed, color):
        self.name = name
        self.age = age
        self.breed = breed
        self.color = color

    def info(self):
        print(self.name, self.age, self.breed, self.color, sep='\n')
        print('#' * 10)

    def run(self):
        print(f"{self.name} is run")

    def sleep(self):
        print(f"{self.name} is sleep")

    def drink(self):
        print(f"{self.name} is drink")

    def eat(self):
        print(f"{self.name} is eat")


ob_1 = Cat("Bob", 2, "home", "white")
ob_2 = Cat("Jack", 3, "home", "yellow")

ob_1.info()
ob_1.run()
ob_1.drink()

ob_2.info()
ob_2.eat()
ob_2.sleep()
