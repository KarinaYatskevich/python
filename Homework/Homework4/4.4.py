

n = int(input())
f1 = 0
f2 = 1
for i in range(int(n-2)):
    print(f1+f2)
    b = f1
    f1 = f2
    f2 = b+f1
print()