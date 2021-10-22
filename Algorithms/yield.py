def y(m):
    for i in m:
        if i % 2 == 0:
            yield i

n = y([1, 2, 3, 4, 5, 6, 7])
print(list(n))


def q():
    for i in range(3):
        yield i*i

print(q())
for i in q():
    print(i)

from time import sleep
from random import randint

def d(a, b):
    b = randint(a, b)
    yield b
    sleep(1)


for i in d(1,100):
    print(i)


