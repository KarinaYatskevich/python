a = input("Введите строку: ")

if len(a) > 10:
    b = input("Введите другую строку: ")
    print(b + "!!!")
elif len(a) < 10:
    print(a[1])