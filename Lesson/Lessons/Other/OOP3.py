class Tomato:
    states = {0: 'nothing', 1: 'flower', 2: 'green_tomato', 3: 'red_tomato'}

    def __init__(self, index):
        self._index = index
        self._state = 0


    def grow(self):
        self._change_state()

    def is_ripe(self):
        if self._state == 3:
            return "all"
        else:
            return "not all"

    def _change_state(self):
        if self._state < 3:
            self._state += 1
        self._print_state()


    def _print_state(self):
        print(f'Tomato {self._index} is {Tomato.states[self._state]}')



class TomatoBush:

    def __init__(self, num):
        self.tomatoes = [Tomato(index) for index in range(0, num-1)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    def give_away_all(self):
        self.tomatoes = []


class Gardener:

    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        print('Work')
        self._plant.grow_all()
        print("Finish")

    def harvest(self):
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print('Harvesting is finished')
        else:
            print('Too early!')

    @staticmethod
    def knowledge_base():
        print('''Harvest time for tomatoes should ideally occur
                    when the fruit is a mature green and
                  ''')

if __name__ == '__main__':
    Gardener.knowledge_base()
    great_tomato_bush = TomatoBush(4)
    gardener = Gardener('Emilio', great_tomato_bush)
    print(gardener.work())
    print(gardener.work())
    print(gardener.harvest())
    print(gardener.work())
    print(gardener.harvest())
