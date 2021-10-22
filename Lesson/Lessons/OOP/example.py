# для импорта надо файл без цифр и подчеркивание только нижнее
class Dog: #Название класса желательно с большой
    __name = ''
    color = ''
    weight = ''
    age = ''
    __master = True
    adress = 'Minsk'


    def __init__(self, name, color, weight, age):
        self.__name = name
        self.color = color
        self.weight = weight
        self.age = age



    def bark(self): #селф нужен везде
        print(f"Woof {self.__name}, color is {self.color}, weight is {self.weight}, age is {self.age}, ")


    def rename(self, new_name): #Изменение атрибутов
        self.__name = new_name

    def set_name(self, new_name):
        if new_name == "Qwerty":
            return
        self.__name = new_name
           # return self.__name

    def get_name(self, new_name):
        return self.__name

    def get_master(self) -> bool: #11.06
        return self.__master

    def get_adress(self):
        return self.__adress

    def set_adress(self, new_adress):
        self.__adress = new_adress



    # def jump(self):
    #     print("Jump!")
    #
    # def run(self):
    #     print("Run!")


def main():
    # dog1 = Dog()
    # print(dog1)
    # dog1.name = "Rax"
    # print(dog1.name)
    # dog1.bark()
    # dog1.jump()
    # dog1.run()
    dog1 = Dog("Rax", "brown", 14, 6) #К деф инит и деф барк это и следующее
    dog1.bark()
    dog1.rename("Qwerty")
    dog1.bark() #Изменение атрибутов это и вверху
    dog1.__name = "test"
    dog1.bark()
    print(dog1.adress)

if __name__ == '__main__':
    main()