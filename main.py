import random


class Animal:
    def __init__(self):
        self.list_animal = ['медведь', 'волк', 'тигр', 'баран', 'крокодил', 'змея', 'носорог', 'курица',
                            'енот', 'кошка']
        self.random_list_animal = random.choice(self.list_animal)
        print(self.random_list_animal)

    def dangerous(self, list_animal):
        pass


class Human(Animal):
    def __init__(self):
        self.list_gun = ['ружье', 'ничего', 'палка', 'топор']
        self.random_list_gun = random.choice(self.list_gun)
        print(self.random_list_gun)

class Fight(Human):


if __name__ == '__main__':
    Animal()
    Human()