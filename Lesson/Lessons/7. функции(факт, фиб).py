# нахождение факториала
def fact(n):
    s = 1
    for i in range(1, n + 1):
        s *= i
    return s

# print(fact(3))

#факториал рекурсивным? методом
def fact_recursive(n):
    if n <= 1:
        return 1
    return n * fact_recursive(n - 1)



# числа фибоначи рекурсивным? способом
def fib(n):
    if n <= 1:
        return 1
    return fib(n - 2) + fib(n - 1)


# print(fib(4))



#сумма всех чисел в кортеже
def print_list(*args):
    print(args)
    s = 0
    for i in args:
        s += i
    return s
# print(print_list(1, 2, 3, 4, 5))



#выводит сумму и самое большое число в кортеже
def sum_items(*args):
    if len(args) <= 0:
        return 0, 0
    s = 0
    max = args[0]

    for i in args:
        s += i
        if i > max:
            max = i

    return s, max
#
# print(sum_items())


# выводит те аргументы, длина ключа которых кратна 2
def my_func(**kwargs):
   for key, value in kwargs.items():
       if len(key) % 2 == 0:
         print(value)


# print(my_func(hello="Ilya", test="Qwerty"))




