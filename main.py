import random


class Animal:
    def __init__(self):
        self.list_animal = ['медведь', 'волк', 'тигр', 'баран', 'крокодил', 'змея', 'носорог', 'курица',
                            'енот', 'кошка']
        self.random_list_animal = random.choice(self.list_animal)


class Human(Animal):
    def __init__(self):
        super().__init__()
        self.list_gun = ['ружье', 'ничего', 'палку', 'топор']
        self.random_list_gun = random.choice(self.list_gun)


class Fight(Human):
    def __init__(self):
        super().__init__()
        print('На арене встречаются {} и человек'.format(self.random_list_animal))
        print('Человек получает {} в качестве оружия'.format(self.random_list_gun))


if __name__ == '__main__':
    Animal()
    Human()
    Fight()