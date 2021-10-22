from time import sleep
from random import randint
import sys
import argparse
import os


# напишем имя и фамилию и год и запишем все в csv файл
parser = argparse.ArgumentParser()
parser.add_argument('-fn', '--first-name', required=True)
parser.add_argument('-ln', '--last-name', required=True)
parser.add_argument('-br', '--born')

args = parser.parse_args()

with open('files/users.csv', 'a') as file:
     file.write(f'{args.first_name},{args.last_name},{args.born}\n')



# напечатает имя и фамилию
# def arg():
#     parser = argparse.ArgumentParser()
#     parser.add_argument('-fn', '--first-name', required=True)  # это каждый столбец. последний пункт - важно или нет
#     parser.add_argument('-ln', '--last-name', required=True)
#
#     args = parser.parse_args()
#     print(args)
#
# if __name__ == '__main__':
#     arg()


# посчитает + или -
# parser = argparse.ArgumentParser()
# parser.add_argument('a', type = int, help = 'first')
# parser.add_argument('b', type = int, help = 'second')
#
# parser.add_argument('-a','--action', help = "why?", default='summ')
#
# args = parser.parse_args()
# print(args)
#
# def summ(a,b):
#     print(a+b)
#
# def min(a,b):
#     print(a - b)
#
# if args.action == 'summ':
#     summ(args.a, args.b)
# elif args.action == 'min':
#     min(args.a, args.b)
# else:
#     print('oooops')





