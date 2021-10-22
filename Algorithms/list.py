a = [1, 2, 3, 4]
print(a[0])
a.append('m')
print(a)
a.remove('m')
print(a)
del a[0]
print(a)
b = []
c = [8, 3]
b.extend(a)
b.extend(c)
print(b)
