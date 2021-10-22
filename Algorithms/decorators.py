def a(func):
    def b(n):
        n = [i for i in n if i% 2 ==0]
        return func(n)
    return b

@a
def l(n):
    print(n)


l([1, 2, 3, 4, 5])
