lst = [7, 3, 2]
n = len(lst)
c = i = 0
while i < n :
    c += (lst[i] + 1) % 2
    i += 1
print(c)

#
# a = [1, 5, 10]
# i = 0
# for n in a:
#     if n % 2 == 0:
#         i += 1
# print(i)