import random


class Animal:
    an_counter = 0

    def __init__(self):
        self.list_animal = ['медведь', 'волк', 'тигр', 'овца', 'крокодил', 'змея', 'носорог', 'курица',
                            'енот', 'кошка']
        self.random_list_animal = random.choice(self.list_animal)

    def random_animal(self):
        return self.random_list_animal


class Human:
    hu_counter = 0

    def __init__(self):
        self.list_gun = ['ружье', 'резиновую уточку', 'палку', 'ядовитый дротик']
        self.random_list_gun = random.choice(self.list_gun)

    def random_gun(self):
        return self.random_list_gun


class Fight:
    def __init__(self):
        self.animal = Animal()
        self.gun = Human()
        print('На арене встречаются {} и человек'.format(self.animal.random_animal()))
        print('Человек получает {} в качестве оружия'.format(self.gun.random_gun()))

    def weapon_inspection(self):
        gun = self.gun.random_gun()
        animal = self.animal.random_animal()
        if (animal == 'енот') or (animal == 'овца') or (animal == 'змея') & (gun != 'резиновую уточку'):
            print('Человек выиграл, +1 очко\n')
            Human.hu_counter += 1
        elif (animal == 'медведь') or (animal == 'волк') or (animal == 'тигр') or (animal == 'крокодил') &\
                (gun == 'ружье') or (gun == 'ядовитый дротик'):
            print('Человек выиграл, +1 очко\n')
            Human.hu_counter += 1
        elif animal == ('кошка' or 'курица'):
            print('Человек выиграл, +1 очко\n')
            Human.hu_counter += 1
        elif animal == 'носорог':
            print('Животное выиграло, +1 очко\n')
            Animal.an_counter += 1
        else:
            print('Животное выиграло, +1 очко\n')
            Animal.an_counter += 1


class Tournament:
    def __init__(self, battles=5):
        self.battles = battles

    def fight(self):
        for round_battles in range(self.battles):
            one = Fight()
            one.weapon_inspection()
        print('Человек выиграл {} раз/а'.format(Human.hu_counter))
        print('Животное выиграло {} раз/а\n'.format(Animal.an_counter))
        if Human.hu_counter > Animal.an_counter:
            print('В этом бою выиграл человек')
        else:
            print('В этом бою выиграло животное')


if __name__ == '__main__':
    two = Tournament()
    two.fight()