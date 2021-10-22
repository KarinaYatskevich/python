n = int(input())
m = int(input())
x = range(n, m)
for i in x:
    for e in range(2, i - 1):
        if i % e == 0:
            print(i, e)