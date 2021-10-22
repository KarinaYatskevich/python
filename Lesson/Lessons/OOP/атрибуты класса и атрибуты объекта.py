# атрибуты класса и атрибуты объекта
class Car:
    last = None

    def __init__(self, model):
        self.model = model
        Car.last = model

if __name__ == '__main__':
     c1 = Car('a')
     print(Car.last)
     c2 = Car('b')
     print(Car.last)
     print(c1.last)
     print(c2.last)
     c3 = Car('hg')
     print(Car.last)
