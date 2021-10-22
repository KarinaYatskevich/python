def fact(n):
    a = 1
    if n % 2 == 0:
        y = 2
        while y <= n:
            a *= y
            y += 2
        return a
    else:
        y = 3
        while y <= n:
            a *= y
            y += 3
        return a


print(fact(10))



fact(10)




