# класс как тип данных
class Point():
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line():
    point_a = None
    point_b = None

    def __init__(self, a: Point, b: Point):
        self.point_a = a
        self.point_b = b

    def lenght(self):
        diff = self.point_a.y - self.point_b.y
        if diff < 0:
            diff = - diff
        return diff


def points():
    line = Line(Point(1,2), Point(1,8))
    print(line.lenght())

if __name__ == '__main__':
    points()