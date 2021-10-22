# import argparse
import time

#
# parser = argparse.ArgumentParser()
#
# parser.add_argument('-n', '--name')
# parser.add_argument('-s', '--surname')
# parser.add_argument('-t', '--time', required=True)
# parser.add_argument('-m', '--minutes', required=True)
# parser.add_argument('-s', '--seconds', required=True)
#
#
#
# args = parser.parse_args()
import time
k = 5
while k != 0:
    print("Осталось времени: {} секунд".format(k))
    k -= 1
    time.sleep(1)

if __name__ == '__main__':
    pass




import time
class Time:

    def __init__(self, first_name, second_name, hours, minutes, seconds):
        self.first_name = first_name
        self.second_name = second_name
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds


# self.seconds += other.seconds
# if self.seconds >= 60:
#     self.minutes += self.seconds // 60
#     self.seconds = self.seconds % 60
#
# self.minutes += other.minutes
# if self.minutes >= 60:
#     self.hours += self.minutes // 60
#     self.minutes = self.minutes % 60
#
# self.hours += other.hours
# return self