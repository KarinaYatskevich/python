#выведет определенную строку из файла
# file = open('files/file.txt', 'r')
# f = file.readlines()
# print(f[2])



# def main():
# Работа с файлами
#    matrix = open("files/matrix.txt") #относительный путь, если написать ./matrix.txt, но он равен и matrix.txt
#    print(matrix)
#    matrix.close() #закрывать надо после себя


#Вывод содержимого файла
   # matrix = open("files/matrix.txt")
   # print(matrix.readlines())
   # matrix.close()

# Построчное чтение (выведет все с файла на в отдельных строках)
#     matrix = open('files/matrix.txt')
#     while True:
#         line = matrix.readline()
#         if not line:
#             break
#         print(line)
#     matrix.close()


# вывести из матрицы:
#     matrix = open("files/matrix.txt")
#     lines = []
#     while True:
#         line = matrix.readline()
#         if not line:
#             break
#         lines.append(line)
#
#
#     matrix.close()
#
#     print(lines[1]) #Первую строку
#     print(lines[-1])  #Последнюю строку
#     print(lines[::2])  #выведет 1 и 3 строку
#     print(lines[:])  #весь файл


# Чтение всех строк файлов
#     matrix = open("files/matrix.txt")
#     print(matrix.readlines())


#Чтение всех строк файла с помощью with
    # with open("files/matrix.txt") as matrix:
    #     for line in matrix.readlines():
    #         print(line)

#запись в файл в конце файла. Можно записать и список (['fghf\n', 'jfndf'])
    # with open("files/matrix.txt", "a") as matrix:
    #     matrix.writelines(['\nquertn\n', 'fhv'])


    # Запись в файл в начало(заменяет все на то, что написано тут)
    # with open("files/matrix.txt", "w") as matrix:
    #  matrix.writelines(['\nquertn\n', 'fhv'])


    # перезапись с 1 файла во второй
    # file_in = open("files/matrix.txt", 'r')
    # file_out = open("files/file2.txt", 'w')
    # file_out.write(file_in.read())


#c одного файла все перезапишет в другой и заменит 1 на 0 и наоборот
# def task():
#     with open('files/file2.txt') as my_file:
#         with open("files/files3.txt", "w") as my_file2:
#           for line in my_file.readlines():
#               print(f"devore {line}")
#               edited = line.replace("0", "@").replace("1", "0").replace("@", "1")
#               print(f"after {line}")
#
#               my_file2.write(edited)






# с одного файла перепишет в другой четные строки, а во второй нечетные
# def task2():
#     with open('files/matrix.txt') as my_file:
#         even = open("files/files4.txt", "w")
#         odd = open("files/files5.txt", "w")
#
#         for index, line in enumerate(my_file.readlines()):
#             diff = (index + 1) % 2
#             if diff == 0:
#                 even.write(line)
#             else:
#                 odd.write(line)
#
#         even.close()
#         odd.close()


# if __name__ == '__main__':




