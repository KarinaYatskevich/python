from random import randint

# counter значение его увеличивается при создании нового любого объекта. Возвращает случайную строку вида A - 2
chars = ['A', 'B', 'C', 'D']

class Car:
        last_model = ''
        __counter = 0

        def __init__(self, model = ''):
            self.model = model
            Car.__counter += 1

        def __len__(self):
            return len(self.model)

        @classmethod #метод класса
        def get_counter(cls):
            return cls.__counter

        @staticmethod
        def is_ok(model):
            return len(model) > 3

        @staticmethod
        def get_random_model():
            char = chars[randint(0, len(chars) - 1)]
            return f'{char}-{randint(1, 100)}'


if __name__ == '__main__':
        car1 = Car(Car.get_random_model())
        Car('b')
        Car('t')
        Car('v')

        print(Car.get_counter())
        print(Car.is_ok(car1))
        print(Car.get_random_model())