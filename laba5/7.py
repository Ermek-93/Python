#Вам дается массив размерности 5х5х3.
# Как его умножить на массив размером 5х5.

import numpy as np
a = np.random.randint(10, size=(5,5))
print(a)
b = np.random.randint(10, size=(5,5,3))
print(b)
c = a*b
print(c)
