def my_decorator(func):
    def wrap(n):
       n = [i for i in n if i % 2 == 0]
       return func(n)

    return wrap

@my_decorator
def real_func(n):
    print(n)


real_func([1, 2, 3, 4, 5, 6, 7, 8])
