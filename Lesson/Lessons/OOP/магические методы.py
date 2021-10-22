# выводит время благодаря магическим методам
from random import randint, choice


class MyTime:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __eq__(self, other):
        return (self.hours == other.hours) and (self.minutes == other.minutes) and (self.seconds == other.seconds)

    def __ne__(self, other):
        return not self.__eq__(self, other)

    def __add__(self, other):
        self.seconds += other.seconds
        if self.seconds >= 60:
            self.minutes += self.seconds // 60
            self.seconds = self.seconds % 60

        self.minutes += other.minutes
        if self.minutes >= 60:
            self.hours += self.minutes // 60
            self.minutes = self.minutes % 60

        self.hours += other.hours
        return self

    def __str__(self):
        return f'{self.hours}:{self.minutes}:{self.seconds}'


def main():
    time1 = MyTime(1, 30, 30)
    time2 = MyTime(1, 70, 80)
    print(time1 + time2)


if __name__ == '__main__':
    main()