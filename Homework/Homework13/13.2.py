import math

class Calculator:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return (self.a == other.a) and (self.b == other.b)



if __name__ == '__main__':
    c = Calculator(3, 5)
    c1 = Calculator(3, 5)
    print(c + c1)
