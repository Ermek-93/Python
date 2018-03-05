#Найти самое часто встречаемое значение в случайном массиве.
import numpy as np
from random import random
N = 15
arr = [0] *N
for i in range(N):
    arr[i] = int(random() *20)
print(arr)
num = arr[0]
max_f = 1
for i in range(N-1):
    f = 1
    for k in range(i+1,N):
        if arr[i] == arr[k]:
         f+=1
    if f > max_f:
        max_f = f
        num = arr[i]

if max_f > 1:
    print(max_f, 'раз(а) встречается число',num)
else:
    print('Все элементы уникальны')