#Создайте случайно заполненный вектор размера N
#  и замените максимальное значение на 0.
import numpy as np
a = np.random.randint(0,10,10)
print(a)
max = a[0]
for i in range(len(a)):
    if max < a[i]:
        max = a[i]
print(max)

