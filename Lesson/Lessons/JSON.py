# JSON
# (закинет словарь в файл)
# import json
# with open('files/matrix.txt', 'w') as my_file:
#  data = json.dumps({'a': 5, 'hbj':3})
#  my_file.write(data)


# выведет содержимое с файла
# with open('files/matrix.txt') as my_file:
 # data = json.loads(my_file.read())
 # print(data)


 # надо разобрать, тк очень часто нужен будет и true в нем пишется с маленькой буквы
 #запишется в json файл
# import json
# def json_01():
#     with open('files/json.json', 'w') as my_file:
#         data = json.dumps({"name": "Ilya", "age": 25})
#         print(data)
#         my_file.write(data)

#создали матрицу случайных чисел и сохранили ее в новом файле. После прочли ее, все четные элементы заменили на 0 и сохранили в другой файл
# import json
# from random import randint
# def task10_07():
#     def create_matrix(n):
#         matrix = []
#         for _ in range(n):
#             row = []
#             for _ in range(n):
#                 row.append(randint(1, 10))
#             matrix.append(row)
#         return matrix
#
#     with open("files/matrix.json", "w") as matrix:
#         matrix = create_matrix(4)
#         matrix.write(json.dumps({"matrix": matrix}))
#
#     with open("files/matrix.json") as matrix:
#         data = json.loads(matrix.read())
#         loaded_matrix = data["matrix"]
#
#         for parentIndex, rows in enumerate(loaded_matrix):
#             for valueIndex, value in enumerate(rows):
#                 if value % 2 == 0:
#                     loaded_matrix[parentIndex][valueIndex] = 0
#
#         print(loaded_matrix)

# в json перезапись с одного файла в другой
# import json
#
# with open('files/matrix.json', 'r') as file:
#     with open('files/file.json', 'w') as file2:
#        file2.write(file.read())
#