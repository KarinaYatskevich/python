
# dct = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
# for k in list(dct.keys()) :
#     dct[k + str(len(k))] = dct.pop(k)
# print(dct)


dct = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
d = {}
i = 0
while len(dct) > i:
    b = dct.keys()
    dct[b + str(len(dct))] = dct.pop(b)
print(dct)
