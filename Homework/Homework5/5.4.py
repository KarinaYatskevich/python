from random import random
N = 19
arr = [0] * N
for i in range(N):
    arr[i] = int(random() * 100)
print(arr)
m = 0
for i in range(2,N,2):
    if arr[i] > arr[m]:
        m = i
print(arr[m])