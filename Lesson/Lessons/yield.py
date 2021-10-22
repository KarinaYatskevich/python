from random import randint
from time import sleep


# итератор
# mylist1 = [1, 2, 3]
# for i in mylist1:
#     print(i)

# mylist2 = [x * x for x in range(3)]
# for i in mylist2:
    # print(mylist2) #напечатает трижды [0, 1, 4]


# генератор
# mygenerator = (x*x for x in range(3))
# for i in mygenerator:
#     print(i) # выведет 0 1 4


#бесконечный генератор случайных чисел с условием 14.02
def create_generator(a, b, c) :
    while True:
        yield randint(a, b)
        a += c
        b += c
        sleep(1)

# if __name__ == '__main__':
#
#     for i in create_generator(0, 4, 2):
#         print(i)



#№2
def create_generator():
    yield 1
    yield 2
    yield 3


# if __name__ == '__main__':
#     # <generator object createGenerator at 0x000000>
#     gen = create_generator()
#     print(f'{next(gen)}!')
#     print(f'{next(gen)}@')


# выведет: корова, кот, собака, медведь, кит
# def my_animal_generator():
#     yield 'корова'
#     for animal in ['кот', 'собака', 'медведь']:
#         yield animal
#     yield 'кит'
#
# my_generator = my_animal_generator()
# print(next(my_generator))
# for animal in my_generator:
    # print(animal)