a = 'hello WoRlD'
print(a.capitalize())
print(len(a))
print(a.swapcase())
print(a.upper())
print(a.title())
print(a.lower())
print(a.count("o"))
print(a.replace('hello', 'hi'))
print('hello' + 'my' + ' ' + 'world')
print(a[0])
print(a.isdigit())
print('42'.isdigit())
print(a.find('l'))
print(a.find('a'))

c ='karina'
b = 'yatskevich'
d = '35'
print(c + ' ' + b + ' ' + d)

x = [1, 2, 3]
z = [4, 5, 6]
z.insert(2, 7)
print(z)
x.extend(z)
print(x)

a = [1, 2, 3, 4]
b = []
print(id(a))
print(id(b))
b = a
print(id(a))
print(id(b))
b.insert(4, 5)
print(b)

a = 'karina'
print(a[2])
print(a[-2])
print(a[:5])
print(a[:-2])
print(a[::-2])

a = 3
b = 5
c = a + b
print(f"{a} + {b} = {c}")

a = 'good day'
b = " ".join(a.split(" "))[::-1]

print("!" + b + '!')

a = ['acv', 'ba']
print([i[::-1] for i in a])

a = [{
    'n': 1,
    'y': 2021
    },
    {
    'n': 2,
    'y': 2025
    }]
print([val for val in a if val["y"] > 2024])

a = {
    'n': 1,
    'y': 2021
    }
print({val: key for key, val in a.items() })

