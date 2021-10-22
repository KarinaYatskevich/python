a = [i for i in range(5)]
# print(a)
b = [i**2 for i in range(5)]
# print(b)


# буквы в списке наоборот
v = ["hello"]
c = [i[::-1] for i in v]
# print(c)

# выведет числа меньше 10
n = [1, 10, 12, 4, 3, 20, 55]
x = [i for i in n if i < 10]
# print(x)


# меньше 10 и возведет в квадрат каждое
s = [i** 2 for i in n if i < 10]
# print(s)


# выведет слова в которых меньше 6 букв
d = ["nano", "marina", "karina", "hey"]
p = [i for i in d if len(i) < 6 ]
# print(p)

# взяли только четные числа и умножили их на 2
g = [i * 2 for i in range(10, 1, -1) if i % 2 == 0]
# print(g)

# добавит точку в конце тех слов, где больше 5 букв
l = ["nano", "marina", "karina", "hey"]
o = [i + "." for i in l if len(i) > 5]
# print(o)


# словарь с машинами. Выводит только те, год выпуска которых больше 2015
q = [
    {
        "num": "ee2",
        "since": 1992,
    },
    {
        "num": "ff2134",
        "since": 1996,
    },
    {
        "num": "ea5",
        "since": 2020,
    },
]
e = [i for i in q if i["since"] > 2015]
# print(e)

# создание матрицы
from random import randint
n = 3

matrix = [[randint(1, 9) for j in range(n)] for i in range(n)]
# print(matrix)

# добавляется количество букв к строке(ключу) (аа2...)
old_dict = {'aa': 1, 'b': 2, 'cccc': 3}
new_dict = {key + str(len(key)): value for key, value in old_dict.items()}
# print(new_dict)

# поменяет местами ключ и значение
h = {'aa': 1, 'b': 2, 'cccc': 3}
m = {value : key for key, value in h.items()}
# print(m)



















