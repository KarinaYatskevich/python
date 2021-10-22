
# from functools import reduce

# фильтрует сначала все числа и выбирает кратные 3, а потом перемножает их
b = list(filter(lambda x: x % 3 == 0,[1,2,3,4,5,6]))
# result = reduce(lambda a, x: a * x, b)
# print(result)


#  посчитает сумму
a = lambda x, y: x + y
# print(a(32, 54))


# напишет привет и имя
b = lambda x: f'Hello {x}'
# print(b("karina"))


# выведет список приветствия
c = lambda x: [b(name) for name in x]
# print(c(["karina", "ilya"]))


# сделает сткокой этот список и они будут в кавычках
# print(list(map(lambda x: str(x), [1, 2, 3])))


# выведет имя в котором есть буква к
# print(list(filter(lambda x: "k" in x, ["karina", "marina"] )))



# выведет it is my code, hello jfj, your
# def a(func):
#     def wrap(n):
#       print('it is my code')
#       func(n)
#       print('your')
#     return wrap
# @a
# def h(n):
#     print('hello', n)
#
#
# h("jfj")


# выведет hello, bob, bye
# def my_decorator(func):
#  def do_some_staff(n):
#    print("hello")
#    result = func(n)
#    print("bye")
#    return result
#  return do_some_staff
#
# @my_decorator
# def my_func(n):
#     print(n)
#     pass
#
#
# my_func("bob")


# декоратор, который выводит время выполнения функции
import time
def calc_time(func):
     def wrap(*args, **kwargs):
        start_at = time.time()
        res = func(*args, **kwargs)
        end_at = time.time()
        print(f'{end_at - start_at}')
        return res
     return wrap

@calc_time
def long(n):
   for _ in range(n):
      pass


@calc_time
def short(n, x):
    for _ in range(n, x):
        pass

long(100600 * 1000)
short(1, x=100)



