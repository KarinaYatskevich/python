import csv
#чтение csv файла
with open('files/csv.csv', newline= '') as line:
    a = csv.DictReader(line)
    for row in a:
        print(row['firstname'], '/',  row['group'])
#запись в csv файл
with open('files/csv2.csv','w', newline= '') as line:
    b = csv.writer(line)
    b.writerow([1, 2, 3])
    b.writerow(['2, 3, 4'])
    b.writerow(['3, 4, 5'])
