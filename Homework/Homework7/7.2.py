while True:

    b = input("1. Дюймы в сантиметры\n2. Сантиметры в дюймы\n3. Мили в километры\n4. Километры в мили\n5. Фунты в килограммы\n6. Килограммы в фунт\n7. Унции в граммы\n8. Граммы в унции\n9. Галлон в литры\n10. Литры в галлоны\n11. Пинты в литры\n12. Литры в пинты\n: ")

    if b == "o":
        break

    c = int(input("Введите исходное число: "))


    if b == "1":

        def inch(c):
          cent = c * 2.54
          print(f'{c} * 2.54 = {cent}')
          return cent


        print(inch(c))

    if b == "2":

       def cent(c):
         inch = c * 0.39
         print(f'{c} * 0.39 = {inch}')
         return inch


       print(cent(c))

    if b == "3":
        def mile(c):
            kilo = c * 1.61
            print(f'{c} * 1.61 = {kilo}')
            return kilo


        print(mile(c))

    if b == "4":
        def kilo(c):
            mile = c * 0.6214
            print(f'{c} * 0.6214 = {mile}')
            return mile


        print(kilo(c))

    if b == "5":
        def lb(c):
            kil = c * 0.4536
            print(f'{c} * 0.4536 = {kil}')
            return kil


        print(lb(c))

    if b == "6":
        def kil(c):
            lb = c * 2.2046
            print(f'{c} * 2.2046 = {lb}')
            return lb


        print(kil(c))

    if b == "7":
        def ounce(c):
            gram = c * 28.3495
            print(f'{c} * 28.3495 = {gram}')
            return gram


        print(ounce(c))

    if b == "8":
        def gram(c):
            ounce = c * 0.0353
            print(f'{c} * 0.0353 = {ounce}')
            return ounce


        print(gram(c))

    if b == "9":
        def gallon(c):
            liter = c * 4.5461
            print(f'{c} * 28.3495 = {liter}')
            return liter


        print(gallon(c))

    if b == "10":
        def liter(c):
            gallon = c * 0.22
            print(f'{c} * 0.22 = {gallon}')
            return gallon


        print(liter(c))

    if b == "11":
        def pints(c):
            litr = c * 0.5683
            print(f'{c} * 0.5683 = {litr}')
            return litr


        print(pints(c))

    if b == "12":
        def litr(c):
            pints = c * 1.7598
            print(f'{c} * 1.7598 = {pints}')
            return pints


        print(litr(c))