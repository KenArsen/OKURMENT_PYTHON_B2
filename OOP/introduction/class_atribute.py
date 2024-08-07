class Product:

    company = "ATA"
    own = "Okurmen"

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def info(self):
        print(f"Name: {self.name}")
        print(f"Price: {self.price}")
        print(f"Company: {self.company}")
        print(f"Own: {self.own}")


product_1 = Product("Apple", 100)
product_2 = Product("Banana", 200)
product_1.info()
print("-" * 10)
product_2.info()
