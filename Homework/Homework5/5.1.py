a = input()
s = 0
i = 1
for n in a:
    s += int(n)
    i *= int(n)
print(s)
print(i)