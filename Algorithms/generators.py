a = ['me', 'you']
print([i[::-1] for i in a])

b = [{'num': 'ab3', 'year': 1998},{'num': 'ab2', 'year': 1995}]
e = [i for i in b if i["year"] > 1997]
print(e)

from random import randint

n = 4
print([[randint(1, 8) for i in range(n)] for j in range(n)])

old_dict = {'aa': 1, 'b': 2, 'cccc': 3}
new_dict = {key + str(len(key)): value for key, value in old_dict.items()}
print(new_dict)

print({value: key for key, value in old_dict.items()})

print({key + str(key): value for key, value in old_dict.items()})

a = ['me', 'you']
print([str(val) + " - " + str(i) for val, i in enumerate(a)])

amb = lambda am: f'Hello {am}'
print(amb(['karina', 'alina']))

an = lambda x: [amb(name) for name in x]
print(an(['karina', 'alina']))

result = map(lambda x: x ** 2, [1,2,3,4,5,6])
print(list(result))

result = list(map(lambda x: str(x), [1,2,3,4,5,6]))
print(list(result))

result = filter(lambda x: x % 2 == 0, [1,2,3,4,5,6])
print(list(result))

result = filter(lambda x: 'k' in x, ['karina', 'marina'])
print(list(result))

from functools import reduce
result = reduce(lambda a, x: a + x ** 2, [1,2,3], 1)
print(result)

d = reduce(lambda a, c: a * a + c, [1, 3, 5, 9], 1)
print(d)
