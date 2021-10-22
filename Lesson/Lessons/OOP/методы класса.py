# методы класса
class Car:
    __last_model = None
    def __init__(self, model):
        self.model = model
        Car.__last_model = model

    @classmethod
    def get_last_model(cls):
        return cls.__last_model

if __name__ == '__main__':
    c = Car('jhg')
    print(Car.get_last_model())