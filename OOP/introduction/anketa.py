class Anketa:
    def __init__(self, name, like_food, hobby, like_sport="Volleyball"):
        self.name = name
        self.like_food = like_food
        self.hobby = hobby
        self.like_sport = like_sport

    def info(self):
        print(f'Name: {self.name}')
        print(f'Like Food: {self.like_food}')
        print(f'Hobby: {self.hobby}')
        print(f'Like Sport: {self.like_sport}')
        print("#" * 20)


ob_1 = Anketa('Alinur', 'Manty', 'Sleep', 'Volleyball')
ob_2 = Anketa('Bilal', 'Oromo', 'Play', 'Soccer')
ob_3 = Anketa('Nurlis', 'Pelmen', 'Swim', 'Basketball')
ob_4 = Anketa('Baiel', 'Kuurdak', 'Watch TV', 'Chess')
ob_5 = Anketa('Arsen', 'Sup', 'Coding')

ob_1.info()
ob_2.info()
ob_3.info()
ob_4.info()
ob_5.info()
