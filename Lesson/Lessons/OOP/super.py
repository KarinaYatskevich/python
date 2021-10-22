# вызов родительского метода (выведет и то, что в родительском и новое)
class Dog:
    def m(self):
        print('nanana')

class Cat(Dog):
    def mainb(self):
        super(Cat, self).m()
        print('lalala')

if __name__ == '__main__':
      c = Cat()
      c.mainb()


