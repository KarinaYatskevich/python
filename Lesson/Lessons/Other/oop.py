class Human:
    default_name = 'No name'
    default_age = 0

    def __init__(self, name=default_name, age = default_age):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = None

    def info(self):
        return f'{self.name}, {self.age}, {self.__money}, {self.__house}'

    @staticmethod
    def default_info():
        return f'{Human.default_name}, {Human.default_age}'

    def __make_deal(self, house, price):
        self.__money -= price
        self.__house = house

    def earn_money(self, earn):
        self.__money += earn
        print(f'earn money {self.__money}')

    def buy_house(self, house, disc):
        price = house.final_price(disc)
        if self.__money >= price:
            self.__make_deal(house, price)
            print("buy")
        else:
            print("nooooo")


class House:

    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, disc):
        final_price = self._price - (100 - disc) / 100
        return final_price


class SmallHouse(House):

    default_area = 40

    def __init__(self, price):
        super(SmallHouse, self).__init__(SmallHouse.default_area, price)








if __name__ == '__main__':
   print(Human.default_info())
   h = Human("Mike", 60)
   print(h.info())
   s = SmallHouse(700)
   print(h.buy_house(s, 25))
   h.earn_money(1000)
   print(h.buy_house(s, 15))
   print(h.info())



