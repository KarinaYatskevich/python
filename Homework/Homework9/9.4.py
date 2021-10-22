def a(func):
    def f(n):
        n = n[::-1]
        return func(n)
    return f

@a
def g(n):
    print(n)

g([1,2,3])




