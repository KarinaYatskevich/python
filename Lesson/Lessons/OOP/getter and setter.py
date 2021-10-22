# декораторы в классах
class Dog:
    __name = ''
    __master = True
    __address = "Minsk"

    def __init__(self, name, color):
        self.__name = name
        self.color = color

    def bark(self):
        print(f"Woof {self.__name}, color is {self.color}")

    def set_name(self, new_name):
        if new_name == "Qwerty":
            return
        self.__name = new_name

    def get_name(self):
        return self.__name

    def get_master(self) -> bool:
        return self.__master
    #
    # @property
    # def address(self):
    #     return self.__address
    #
    # @address.setter
    # def address(self, new_address):
    #     print("Im here")
    #     self.__address = new_address

    def get_address(self): # = тому, что написано через декораторы
        return self.__address

    def set_address(self, new_address):
        print('im hear')
        self.__address = new_address



def main():
    dog1 = Dog("Rax", "brawn")
    dog1.bark()
    dog1.set_name("Qwerty")
    dog1.bark()
    print(dog1.get_name())
    # print(dog1.address) #если писать через декораторы
    # dog1.address = "Riga"
    # print(dog1.address)
    print(dog1.get_address()) #если писать через гетеры и сетеры
    dog1.set_address("riga")
    print(dog1.get_address())



if __name__ == '__main__':
    main()