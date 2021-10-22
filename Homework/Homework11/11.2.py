class Car:
    __make = ''
    __model = ''
    __year = ''
    __speed = 0

    def __init__(self, make, model, year, speed):
        self.__make = make
        self.__model = model
        self.__year = year
        self.__speed = speed


    def bark(self):
        print(f"Car make: {self.__make}, car model: {self.__model}, year: {self.__year}, speed: {self.__speed} ")


    def increase(self, increase):
        s = int(increase) + 5
        print(s)

    def decrease(self, decrease):
        s = int(decrease) - 5
        print(s)

    def stop(self, stop):
        print(0)

    def display(self, n):
        print(n)

    def u_turn(self,n):
        if n > 0:
            print(-n)
        elif n < 0:
            print(-n)

c = Car("BMW", "s-class", "2014", 0)
c.bark()
c.increase(95)
c.decrease(95)
c.stop(25)
c.display(99)
c.u_turn(-65)
