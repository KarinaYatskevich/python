import sys

# выведет в командной строке сумму чисел (писать их надо в ней через пробел). Если будет буква, пропустит ее
def main():
    numbers = sys.argv[1:]
    sum = 0
    for item in numbers:
        if not item.isdigit():
            continue

        sum += int(item)

    print(sum)

if __name__ == '__main__':
    print(main())


# print(sys.argv) #выведет полный путь к этому файлу
# if 'Alex' in sys.argv:
#     print('Hello, Alex')
# else:
#     print('Hello, Guest')