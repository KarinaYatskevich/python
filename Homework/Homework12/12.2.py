import math
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y
class Figure:
    pass

class Circle(Figure):

    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

    def area(self):
        return 3.14 * (self.radius ** 2)


class Triangle(Figure):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        return (1/2) * self.a * self.b

    def perimeter(self):
        return self.a + self.b + self.c


def main():
    circle = Circle(5)
    print(round(circle.perimeter()))
    print(circle.area())
    triangle = Triangle(5, 6, 7)
    print(triangle.area())
    print(triangle.perimeter())


if __name__ == '__main__':
    main()


