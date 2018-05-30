import random


class Animal:
    an_counter = 0

    def __init__(self):
        self.list_animal = ['медведь', 'волк', 'тигр', 'овца', 'крокодил', 'змея', 'носорог', 'курица',
                            'енот', 'кошка']
        self.random_list_animal = random.choice(self.list_animal)


class Human(Animal):
    hu_counter = 0

    def __init__(self):
        super().__init__()
        self.list_gun = ['ружье', 'ничего', 'палку', 'ядовитый дротик']
        self.random_list_gun = random.choice(self.list_gun)


class Fight(Human):
    def arena(self):
        print('На арене встречаются {} и человек'.format(self.random_list_animal))
        print('Человек получает {} в качестве оружия'.format(self.random_list_gun))

    def weapon_inspection(self):
        gun = self.random_list_gun
        animal = self.random_list_animal
        if (animal == 'енот') or (animal == 'овца') or (animal == 'змея') & (gun != 'ничего'):
            print('Человек выиграл, +1 очко\n')
            Human.hu_counter += 1
        elif (animal == 'медведь') or (animal =='волк') or (animal == 'тигр') or (animal == 'крокодил') &\
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


class Victory:
    def __init__(self, battle=0):

        while battle < 5:
            one = Fight()
            one.arena()
            one.weapon_inspection()
            battle += 1
        print('Человек выиграл {} раз/а'.format(Human.hu_counter))
        print('Животное выиграло {} раз/а\n'.format(Animal.an_counter))
        if Human.hu_counter > Animal.an_counter:
            print('В этой бою выиграл человек')
        else:
            print('В этом бою выиграло животное')


if __name__ == '__main__':
    Victory()
