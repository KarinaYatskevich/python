
while True:
    x = int(input("1: "))
    y = int(input("2: "))
    a = input("(+, -, /, *): ")
    if a == "o":
        break
    if a == "+":
        print(x + y)
    elif a == "-":
        print(x-y)
    elif a == "/":
        if y != 0:
            print(x / y)
        else:
            print("ошибка")

    elif a == "*":
        print(x * y)















