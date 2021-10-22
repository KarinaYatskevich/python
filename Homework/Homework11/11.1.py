class Cat:
    __name = ""
    __age = ""
    __country = ""
    color = ""

    def __init__(self, name, age, country, color):
        self.__name = name
        self.__age = age
        self.__country = country
        self.color = color

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def get_country(self):
        return self.__country

    def set_country(self, country):
        self.__country = country

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color



# cat1 = Cat("max", 4, "Belarus", "blue")
# print(cat1._Cat__name) #выведет имя кота из привата
# print(cat1.color) #выведет цвет кота

c = Cat("Mark", 7, "belarus", "blue")
print(c.get_age())
print(c.get_name())
print(c.get_country())
print(c.get_color())
c.set_name("Pavel")
c.set_age(9)
c.set_country("USA")
c.set_color("pink")
print(c.get_name())
print(c.get_age())
print(c.get_country())
print(c.get_color())



class Dog:
    __name = ""
    __age = ""
    __country = ""
    color = ""

    def __init__(self, name, age, country, color):
        self.__name = name
        self.__age = age
        self.__country = country
        self.color = color

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def get_country(self):
        return self.__country

    def set_country(self, country):
        self.__country = country

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color


d = Dog("Max", 10, "Belarus", "gray")
print(d.get_age())
print(d.get_name())
print(d.get_country())
print(d.get_color())
d.set_name("Nikita")
d.set_age(8)
d.set_country("Russia")
d.set_color("yellow")
print(d.get_name())
print(d.get_age())
print(d.get_country())
print(d.get_color())



