
# наследование и сравнение 2-х функций
class Animal:
    name = ''
    age = 0
    master = False
    weight = 0
    height = 0

    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master

    def run(self):
        print(f'{self.name}, running')

    def jump(self):
        print(f'{self.name}, jumping')

    def birthday(self):
        self.age += 1

    def change_weight(self, new_weight=0):
        if not new_weight:
            new_weight = 0.2
        self.weight += new_weight

    def change_height(self, new_height=0):
        if not new_height:
            new_height = 0.2
        self.height += new_height

    def voice(self, voice): #не добавляется в инит и является пустым методом, поэтому добавляется потом в каждый класс
        print(f'{self.name}, {voice}')


class Dog(Animal):
    test = ''

    def run(self):
        if self.weight > 0.3:
            print('too fat!')
            return
        else:
            super().run()

    def bark(self):
        print(f'{self.name}, bark!')

    def jump(self, height=0):
        if height > 0.5:
            print('Dog cannot jump too height')
            return
        super(Dog, self).jump()

    def voice(self):
        super(Dog, self).voice('bark!')


class Cat(Animal):
    def meow(self):
        print(f'{self.name}, meow!')

    def voice(self):
        super(Cat, self).voice('meow!')


class Parrot(Animal):
    species = ''

    def fly(self):
        if self.weight > 0.1:
            print('Parrot cannot fly!')
            return
        print(f'{self.name}, fly!')


def main():
    dog = Dog('rax', 7, False)
    dog2 = Dog('qwertyu', 6, True)
    print(f'dog2 > dog1 :{dog2.age > dog.age}')
    dog.run()
    dog.jump()
    dog.change_height()
    dog.change_weight()
    dog.voice()
    dog.run()
    dog.weight = 8
    dog.run()
    cat = Cat('lary', 8, True)
    cat.run()
    cat.voice()
    cat.meow()
    parrot = Parrot('Max', 9, False)
    parrot.run()
    print(dir(parrot)) #выводит все об объекте


if __name__ == '__main__':
        main()