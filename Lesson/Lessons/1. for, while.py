# выведет отдельно все буквы слова
for x in "Banan":
 print(x)



# сумма чисел больше 10
a =[2, 6, 10, 17, 13]

accum = 0

for item in a:
   if item > 10:
       accum += item

print(accum)



# если число, то ничего, а если стоп, то выводит 0??
acc = 0
while True:
   a = input("ведите число: ")
   if not a.isdigit():

     if a == "стоп":
       break
       continue
       acc += int(a)

print(acc)



# выведет числа от 2 до 5 включительно
a, b = 2, 5

lst = range(a, b+1)
count = len(lst)

for i in lst:
   print(i)

print("count is {count}")



# напишет привет илья
def say_hello(name):
 return f"Hello, {name}"
print(say_hello("Ilya") )



# выведет числа от 1 до 5 включительно в обратном порядке
a = 5
while a > 0:
 print(a)
 a -= 1





