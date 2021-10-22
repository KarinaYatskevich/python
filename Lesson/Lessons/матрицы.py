
# создание простой матрицы
from random import randint as get_rand

def create_matrix(x, y):
    rows = []
    for _ in range(x):
        tmp = []
        for _ in range(y):
            tmp.append(get_rand(0, 10))
        rows.append(tmp)

    return rows
print(create_matrix(5, 2))

# создание матрицы ( какое значение , столько и цифр, строк(5 => 5*5))
def create_square_matrix(length):
    return create_matrix(length, length)
# print(create_square_matrix(5))


def sum_of_matrix_elements_by_divider(matrix, divider):
    sum = 0
    for parentList in matrix:
        for matrixItem in parentList:
            if matrixItem % divider == 0:
                sum += matrixItem
    return sum

# square_matrix = create_square_matrix(3) # создание матрицы ( какое значение , столько и цифр, строк(5 => 5*5))
# print(square_matrix)
# print(sum_of_matrix_elements_by_divider(square_matrix, 3)) # в матрице находит числа кратные 3 и выводит их сумму
#
def count_in_matrix(matrix, to_find):
    count = 0
    for parentList in matrix:
        for matrixItem in parentList:
            if matrixItem == to_find:
                count += 1
    return count

# matrix = create_matrix(2, 3) #создаст матрицу с 2 строками и 3 цифрами в строке
# print(matrix)
# print(count_in_matrix(matrix, 2))  #напишет сколько чисел в матрице =2
# #
# matrix = create_matrix(2, 3) #создаст матрицу с 2 строками и 3 цифрами в строке

def calc_av_sum(matrix):
    count = 0
    sum = 0
    for parentList in matrix:
        for matrixItem in parentList:
            count += 1
            sum += matrixItem
    avv = sum / count
    return avv

# average = calc_av_sum(matrix)
# print(matrix)
# print(average) #находит среднее арифметическое от всех чисел в матрице
#
def calc_elements(matrix, average):
    count = 0
    for parentIndex, parentList in enumerate(matrix):
        print(f"parentInx: {parentIndex}, parent: {parentList}")
        for childIndex, child in enumerate(parentList):
            print(f"childInx: {childIndex}, child: {child}")
            if child > average and (parentIndex + childIndex) % 2 == 0:
                count += 1
    return count

print(calc_elements(matrix, average)) # c 62 до 72 не работает, поэтому не знаю что тут происходит


from random import randint

def create_matrix(weight=2, height=2): #Создание матрицы
    matrix = []
    for _ in range(0, weight):
        row = []
        for _ in range(0, height):
            row.append(randint(0, 10))
        matrix.append(row)
    return matrix
#
#
# matrix = create_matrix()
#
#
def print_matrix(matrix): #Вывод чисел из матрицы
    for vert in matrix:
        for item in vert:
            print(f"Element is \"{item}\"")
#
#
# print_matrix(matrix)


def sum_matrix(matrix): #Сумма всех элементов матрицы
    acc = 0
    for vert in matrix:
        for item in vert:
            acc += item
    return acc
#
#
# # print(sum_matrix(matrix))
#
#
def min(matrix): #Нахождение максимального элемента матрицы
    min = matrix[0][0]
    for vert in matrix:
        for item in vert:
            if item < min:
                min = item
    return min
#
#
# print(matrix)
# print(min(matrix))
#
#
def max(matrix): #Нахождение минимального элемента матрицы
    max = matrix[0][0]
    for vert in matrix:
        for item in vert:
            if item > max:
                max = item
    return max


# print(matrix)
# # print(max(matrix))


